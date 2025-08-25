import re
from textnode import TextNode, TextType


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    new_list_of_nodes = split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter([text_node], "**", TextType.BOLD),
                    "_",
                    TextType.ITALIC,
                ),
                "`",
                TextType.CODE,
            )
        )
    )
    return new_list_of_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text_list = node.text.split(delimiter)
        if len(split_text_list) % 2 == 0:
            raise Exception("Invalid Markdown syntax: missing closing delimiter")
        for index, string in enumerate(split_text_list):
            if index % 2 == 0:
                new_nodes.append(TextNode(string, TextType.TEXT))
            elif string == "":
                continue
            else:
                new_nodes.append(TextNode(string, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        after = node.text
        while True:
            images = extract_markdown_images(after)
            if len(images) == 0:
                if after:
                    new_nodes.append(TextNode(after, TextType.TEXT))
                break
            image_alt, image_link = images[0]
            section = after.split(f"![{image_alt}]({image_link})", 1)
            if len(section) != 2:
                raise Exception(
                    "Invalid markdown syntax: image section not properly closed"
                )
            before = section[0]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            after = section[1]
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        after = node.text
        while True:
            links = extract_markdown_links(after)
            if len(links) == 0:
                if after:
                    new_nodes.append(TextNode(after, TextType.TEXT))
                break
            link_name, actual_link = links[0]
            section = after.split(f"[{link_name}]({actual_link})", 1)
            if len(section) != 2:
                raise Exception(
                    "Invalid markdown syntax: link section not properly closed"
                )
            before = section[0]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link_name, TextType.LINK, actual_link))
            after = section[1]
    return new_nodes
