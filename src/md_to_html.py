from extract_markdown import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode


def mardown_to_html_node(markdown):
    blocked_markdown = markdown_to_blocks(markdown)
    for block in blocked_markdown:
        type_of_block = block_to_block_type(block)
        if type_of_block == BlockType.QUOTE:
            HTMLNode(
                "blockquote",
            )
