from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        split_text_list = node.text.split(delimiter)
        if len(split_text_list) % 2 == 0:
            raise Exception("Invalid Markdown syntax: missing closing delimiter")
        for index, string in enumerate(split_text_list):
            if index % 2 == 0:
                new_nodes.append(TextNode(string, TextType.TEXT))
            elif string == "":
                pass
            else:
                new_nodes.append(TextNode(string, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)

        after = node.text
        while True:
            images = extract_markdown_images(after)
            if not images:
                break
            image_alt, image_link = images[0]
            section = after.split(f"![{image_alt}]({image_link})", 1)
            before = section[0]
            new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            if len(section) == 1:
                new_nodes.append(TextNode(section[0], TextType.TEXT))
                break
            after = section[1]
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)

        after = node.text
        while True:
            links = extract_markdown_links(after)
            if not links:
                break
            link_name, actual_link = links[0]
            section = after.split(f"[{link_name}]({actual_link})", 1)
            before = section[0]
            new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link_name, TextType.LINK, actual_link))
            if len(section) == 1:
                new_nodes.append(TextNode(section[0], TextType.TEXT))
                break
            after = section[1]
    return new_nodes


print(
    split_nodes_image(
        [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
        ]
    )
)


print(
    split_nodes_link(
        [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
            )
        ]
    )
)
