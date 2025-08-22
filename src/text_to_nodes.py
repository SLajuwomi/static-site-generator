from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    # new_list_of_nodes = split_nodes_link(
    #     split_nodes_image(
    #         split_nodes_delimiter(
    #             split_nodes_delimiter(
    #                 split_nodes_delimiter([text_node], "**", TextType.BOLD),
    #                 "_",
    #                 TextType.ITALIC,
    #             ),
    #             "`",
    #             TextType.CODE,
    #         )
    #     )
    # )
    bold_text = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    for bold in bold_text:
        print(bold)
    italic_text = split_nodes_delimiter(bold_text, "_", TextType.ITALIC)
    print()
    for italic in italic_text:
        print(italic)
    code_text = split_nodes_delimiter(italic_text, "`", TextType.CODE)
    print()
    for code in code_text:
        print(code)
    split_images = split_nodes_image(code_text)
    print()
    for line in split_images:
        print(line)
    split_links = split_nodes_link(split_images)
    print()
    for thing in split_links:
        print(thing)


text_to_textnodes(
    "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
)
