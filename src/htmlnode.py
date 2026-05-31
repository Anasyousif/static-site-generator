class HTMLNode:
    def __init__(self,tag=None, value=None, childern=None, props=None):
        self.tag = tag
        self.value = value
        self.childern = childern if childern is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementError("to_html method not implemented")
    def props_to_html(self):
        if not self.props:
            return ""
        html_attributes = []
        for key , value in self.props.items():
            html_attributes.append(f'{key}="{value}"')
        return " " + " ".join(html_attributes)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, childern: {self.childern}, {self.props})"
    class LeafNode(HTMLNode):
        def __init__(self , tag, value, props=None):
            super().__init__(tag = tag, vlaue=value, childern=None,props=props)
        def to_html(self):
            if self.value is None:
                raise ValueError("All leaf nodes must have a value.")
            if self.tag is None:
                return self.value
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        def __repr__(self):
            return  f"LeafNode({self.tag}, {self.value}, {self.props})"  