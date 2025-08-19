from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return self.value

        final_string = ""
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        print(super().props_to_html())
        return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
