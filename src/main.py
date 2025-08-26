import os
import shutil
from textnode import TextNode
from textnode import TextType


def main():
    src_to_dst("../static", "../public")


def src_to_dst(src, dst):
    shutil.rmtree(dst)
    os.mkdir(dst)
    # print(os.listdir(src))
    # print(os.listdir(dst))
    for item_name in os.listdir(src):
        item_path = os.path.join(src, item_name)
        print(f"Current item path: {item_path}")
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst=dst)
        elif os.path.isdir(item_path):
            os.mkdir(f"{dst}/{item_name}")
            src_to_dst(item_path, dst=f"{dst}/{item_name}")
    print(f"At end {os.listdir(dst)}")


if __name__ == "__main__":
    main()
