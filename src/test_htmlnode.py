import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        print(node.props_to_html())

        node2 = HTMLNode(
            tag="p",
            value="Lorem ipsum",
            children=[
                HTMLNode(
                    tag="a",
                    value="google.com",
                    props={"href": "www.google.com", "target": "_blank"},
                )
            ],
            props={"format": "bold"},
        )

        print(node2)
        print(node2.props_to_html())
