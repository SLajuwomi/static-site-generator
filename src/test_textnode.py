import unittest

from textnode import TextNode, TextType
from extract_markdown import text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a bad node", TextType.ITALIC)
        node4 = TextNode("This is a good node", TextType.ITALIC)
        self.assertNotEqual(node3, node4)
        node5 = TextNode("bold node", TextType.BOLD)
        node6 = TextNode("link", TextType.LINK)
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This should not work", TextType.CODE)

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_invalid_type(self):
        node = TextNode("This is a text that should fail", "text")
        with self.assertRaises(Exception):
            node.text_node_to_html_node()


if __name__ == "__main__":
    unittest.main()
