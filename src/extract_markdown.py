import re


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def markdown_to_blocks(markdown):
    list_markdown = markdown.split("\n\n")
    new_list = [item.strip() for item in list_markdown if item is not ""]
    return new_list
