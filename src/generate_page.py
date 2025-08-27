import os
from markdown_blocks import markdown_to_html_node
from extract_markdown import extract_title


def generate_page(from_path, dest_path, template_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as f:
        template_content = f.read()
    markdown_node = markdown_to_html_node(markdown_content)
    markdown_string = markdown_node.to_html()
    markdown_title = extract_title(markdown_content)
    with_title = template_content.replace("{{ Title }}", markdown_title)
    with_content = with_title.replace("{{ Content }}", markdown_string)
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(with_content)
