from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAIN:
            new_nodes.append(node)
        split_text_list = node.text.split(delimiter)
        if len(split_text_list) % 2 == 0:
            raise Exception("Invalid Markdown syntax: missing closing delimiter")
        for index, string in enumerate(split_text_list):
            if index % 2 == 0:
                new_nodes.append(TextNode(string, TextType.PLAIN))
            elif string == "":
                pass
            else:
                new_nodes.append(TextNode(string, text_type))

    return new_nodes


node = TextNode("This is a text with a `code block` word", TextType.PLAIN)
split_nodes_delimiter([node], "`", TextType.CODE)
