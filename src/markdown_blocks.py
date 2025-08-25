from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode


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
    print(f"Blocked Markdown: {blocked_markdown}")
    for block in blocked_markdown:
        type_of_block = block_to_block_type(block)
        list_items = block.split("\n")
        print(f"Block:\n{block}")
        print(f"Block Type: {type_of_block}")
        print(f"List Items: {list_items}")
        if type_of_block == BlockType.QUOTE:
            new_html_node = HTMLNode("blockquote", block)
        if type_of_block == BlockType.HEADING:
            for char in block:
                if char == "#":
                    heading_count += 1
                else:
                    break
            new_html_node = HTMLNode(f"h{heading_count}", block)
        if type_of_block == BlockType.PARAGRAPH:
            new_html_node = LeafNode("p", block)
            print(new_html_node.to_html())
        if type_of_block == BlockType.CODE:
            code_content = "\n".join(list_items[1:-1])
            code_node = LeafNode("code", code_content)
            pre_node = ParentNode("pre", children=[code_node])
            # print(pre_node.to_html())
        if type_of_block == BlockType.ULIST:
            li_nodes = [
                LeafNode("li", item.lstrip("- ").strip()) for item in list_items
            ]
            ul_node = ParentNode("ul", children=li_nodes)
            # print(ul_node.to_html())


# markdown = """
# - Item 1
# - Item 2
# - Item 3
# """
markdown = """
This is some random paragraph text
some more random text
"""
nodes = markdown_to_html_node(markdown)
print(nodes)
