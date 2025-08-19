import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
