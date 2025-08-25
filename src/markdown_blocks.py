from enum import Enum
from htmlnode import HTMLNode


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
    for block in blocked_markdown:
        type_of_block = block_to_block_type(block)
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
            new_html_node = HTMLNode("p", block)
        if type_of_block == BlockType.CODE:
            continue
