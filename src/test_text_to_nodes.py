import unittest

from text_to_nodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        heavily_nested = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        heavily_nested_result = text_to_textnodes(heavily_nested)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            heavily_nested_result,
        )

    def test_actually_nested_string(self):

        actually_nested = "This is an **_italic line_ inside of a bolded line** with link to [therapy](www.calmi.so) for good measure."
        actually_nested_result = text_to_textnodes(actually_nested)
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("_italic line_ inside of a bolded line", TextType.BOLD),
                TextNode(" with link to ", TextType.TEXT),
                TextNode("therapy", TextType.LINK, "www.calmi.so"),
                TextNode(" for good measure.", TextType.TEXT),
            ],
            actually_nested_result,
        )
