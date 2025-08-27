import os
import shutil

from generate_page import generate_page, generate_pages_recursive


def main():
    src_to_dst("static", "public")


def src_to_dst(src, dst):
    shutil.rmtree(dst)
    os.mkdir(dst)
    for item_name in os.listdir(src):
        item_path = os.path.join(src, item_name)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst=dst)
        elif os.path.isdir(item_path):
            os.mkdir(f"{dst}/{item_name}")
            src_to_dst(item_path, dst=f"{dst}/{item_name}")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
