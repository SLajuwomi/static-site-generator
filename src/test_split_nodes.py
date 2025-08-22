import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
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
