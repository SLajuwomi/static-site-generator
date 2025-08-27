from enum import Enum
from extract_markdown import text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown):
    list_markdown = markdown.split("\n\n")
    new_list = [item.strip() for item in list_markdown if item != ""]
    return new_list


def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("-"):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocked_markdown = markdown_to_blocks(markdown)
    blocked_nodes = []
    for block in blocked_markdown:
        type_of_block = block_to_block_type(block)
        list_items = block.split("\n")
        if type_of_block == BlockType.QUOTE:
            stripped_list = [item.lstrip("> ").strip() for item in list_items]
            stripped_block = "\n".join(stripped_list)
            quote_node = LeafNode("blockquote", stripped_block)
            blocked_nodes.append(quote_node)
        if type_of_block == BlockType.HEADING:
            heading_count = 0
            for char in block:
                if char == "#":
                    heading_count += 1
                else:
                    break
            stripped_list = [
                item.lstrip("#" * heading_count + " ").strip() for item in list_items
            ]
            stripped_block = "\n".join(stripped_list)
            heading_node = LeafNode(f"h{heading_count}", stripped_block)
            blocked_nodes.append(heading_node)
        if type_of_block == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            children = text_to_children(block)
            paragraph_node = ParentNode("p", children)
            blocked_nodes.append(paragraph_node)
        if type_of_block == BlockType.CODE:
            code_content = "\n".join(list_items[1:-1])
            code_content += "\n"
            text_code_node = TextNode(code_content, TextType.CODE)
            text_code_html_node = text_code_node.text_node_to_html_node()
            pre_node = ParentNode("pre", children=[text_code_html_node])
            blocked_nodes.append(pre_node)
        if type_of_block == BlockType.ULIST:
            li_nodes = []
            for item in list_items:
                text = item.lstrip("- ").strip()
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            ul_node = ParentNode("ul", children=li_nodes)
            blocked_nodes.append(ul_node)
        if type_of_block == BlockType.OLIST:
            i = 1
            li_nodes = []
            for item in list_items:
                text = item.lstrip(f"{i}. ").strip()
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
                i += 1
            ol_node = ParentNode("ol", children=li_nodes)
            blocked_nodes.append(ol_node)
    div_node = ParentNode("div", blocked_nodes)
    return div_node


def text_to_children(text):
    # import re

    # children = []
    # patterns = [
    #     (r"\*\*(.*?)\*\*", TextType.BOLD),
    #     (r"_(.*?)_", TextType.ITALIC),
    #     (r"`(.*?)`", TextType.CODE),
    # ]
    # pos = 0
    # while pos < len(text):
    #     match = None
    #     for pattern, text_type in patterns:
    #         match = re.search(pattern, text[pos:])
    #         if match:
    #             # if greater than 0, there was text between the last pos and the start of the string
    #             if match.start() > 0:
    #                 children.append(
    #                     TextNode(text[pos : pos + match.start()], TextType.TEXT)
    #                 )
    #             children.append(TextNode(match.group(1), text_type))
    #             pos += match.end()
    #             break
    #     if not match:
    #         children.append(TextNode(text[pos:], TextType.TEXT))
    #         break
    # return [child.text_node_to_html_node() for child in children]

    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node.text_node_to_html_node()
        children.append(html_node)
    return children
