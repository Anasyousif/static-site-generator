class HTMLNode:
    def __init__(self,tag=None, value= None, childern=None, props= None):
        self.tag = tag
        self.value = value
        self.childern = childern if childern si not None else []
    def to_html(self):
        raise NotImplementError("to_html method implemented")
    def props_to_html(self):
        if not self.props:
            return ""
        html_attributes = []
        for key , value in self.props.items():
            html_attributes.append(f'{key}="{value}"')
        return " " + " ".join(html_attributes)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, childern: {self.childern},{self.props})"