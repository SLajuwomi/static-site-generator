import unittest

from extract_markdown import (
    extract_markdown_images,
    extract_markdown_links,
)
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks
from extract_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestExtractMarkdown(unittest.TestCase):
    def test_split_nodes(self):
        code_node = TextNode("This is a text with a `code block` word", TextType.TEXT)
        italic_node = TextNode("This is _an italic word_.", TextType.TEXT)
        italic_nested_bold_node = TextNode(
            "This is an _italic and **bold** word_.", TextType.TEXT
        )
        bold_node = TextNode("This is a **bold** node", TextType.TEXT)

        self.assertEqual(
            split_nodes_delimiter(
                old_nodes=[code_node], delimiter="`", text_type=TextType.CODE
            ),
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

        self.assertEqual(
            split_nodes_delimiter(
                old_nodes=[italic_node], delimiter="_", text_type=TextType.ITALIC
            ),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("an italic word", TextType.ITALIC),
                TextNode(".", TextType.TEXT),
            ],
        )

        self.assertEqual(
            split_nodes_delimiter(
                old_nodes=[italic_nested_bold_node],
                delimiter="_",
                text_type=TextType.ITALIC,
            ),
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("italic and **bold** word", TextType.ITALIC),
                TextNode(".", TextType.TEXT),
            ],
        )

        self.assertEqual(
            split_nodes_delimiter(
                old_nodes=[bold_node], delimiter="**", text_type=TextType.BOLD
            ),
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" node", TextType.TEXT),
            ],
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and another [neovim](www.gogoogleitnoob.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("neovim", TextType.LINK, "www.gogoogleitnoob.com"),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a link to [google](www.google.com) and a link to [Github](www.github.com)."
        )
        self.assertListEqual(
            [("google", "www.google.com"), ("Github", "www.github.com")], matches
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = """


This is an _italic_ line.
This is a line next to italic line.

Testing double new line.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is an _italic_ line.\nThis is a line next to italic line.",
                "Testing double new line.",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
