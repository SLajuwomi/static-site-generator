import os
import shutil
import sys

from generate_page import generate_page, generate_pages_recursive

basepath = sys.argv[1]


def main():
    src_to_dst("static", "public")


def src_to_dst(src, dst):
    print("Deleting public directory...")
    shutil.rmtree(dst)
    os.mkdir(dst)
    print("Copying static files to public directory...")
    for item_name in os.listdir(src):
        item_path = os.path.join(src, item_name)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst=dst)
        elif os.path.isdir(item_path):
            os.mkdir(f"{dst}/{item_name}")
            src_to_dst(item_path, dst=f"{dst}/{item_name}")
    print("Generating content...")
    generate_pages_recursive("content", "template.html", "public", basepath)


if __name__ == "__main__":
    main()
