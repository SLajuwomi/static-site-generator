import os
import shutil
import sys

from generate_page import generate_page, generate_pages_recursive

basepath = sys.argv[1]
dir_path_static = "static"
dir_path_public = "docs"
dir_path_content = "content"
template_path = "template.html"


def main():
    src_to_dst(dir_path_static, dir_path_public)


def src_to_dst(src, dst):
    print("Deleting docs directory...")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    print("Copying static files to docs directory...")
    for item_name in os.listdir(src):
        item_path = os.path.join(src, item_name)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst=dst)
        elif os.path.isdir(item_path):
            os.mkdir(f"{dst}/{item_name}")
            src_to_dst(item_path, dst=f"{dst}/{item_name}")
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


if __name__ == "__main__":
    main()
