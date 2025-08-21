import unittest

from textnode import TextNode, TextType


class TestTextToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_invalid_type(self):
        node = TextNode("This is a text that should fail", "plain")
        with self.assertRaises(Exception):
            node.text_node_to_html_node()
