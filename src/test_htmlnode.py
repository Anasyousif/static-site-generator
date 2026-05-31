import unittest 
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_formatting(self):
        node = HTMLNode(
            tag="a",
            props={"href":"https://wwww.google.com","target":"_blank"}
        )
        self.assertEqual(
            node.props_to_html(),' href="https://wwww.google.com" target="_blank"'
        )
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")
    def test_repr_output(self):
        node = HTMLNode(
            tag="p",
            value="Hello World",
            props={"class": "paragraph"}
        )
        expected_repr = "HTMLNode(p, Hello World, childern: [], {'class': 'paragraph'})"
        self.assertEqual(repr(node), expected_repr)
if __name__ == "__main__":
    unittest.main()