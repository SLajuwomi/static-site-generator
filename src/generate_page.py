import os
from pathlib import Path
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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path_content):
        for filename in filenames:
            full_file_path = os.path.join(dirpath, filename)
            rel_file_path = os.path.relpath(full_file_path, dir_path_content)
            html_rel_file_path = rel_file_path.replace("md", "html")
            complete_dest_dir_path = os.path.join(dest_dir_path, html_rel_file_path)
            parts = complete_dest_dir_path.split(os.sep)
            current_path = ""
            for part in parts:
                if not part:
                    continue
                current_path = os.path.join(current_path, part)
                path_obj = Path(current_path)
                if not os.path.isdir(current_path) and not bool(path_obj.suffix):
                    os.makedirs(current_path, exist_ok=True)
            # print(complete_dest_dir_path)
            # print(rel_file_path)
            # print(html_rel_file_path)
            # print(f"File: {full_file_path}")
            if full_file_path.endswith("md"):
                generate_page(
                    full_file_path,
                    complete_dest_dir_path,
                    template_path,
                )
            else:
                continue


# generate_pages_recursive("../content", "../template.html", "../public/")
