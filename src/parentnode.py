from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have a tag")

        if self.children == None:
            raise ValueError("There are no children")

        list_of_children = ""
        for child in self.children:
            list_of_children += child.to_html()
        return f"<{self.tag}>{list_of_children}</{self.tag}>"
