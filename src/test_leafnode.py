import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_tag(self):
        # Verifies that a node with no tag returns just raw text
        node = LeafNode(None, "This is just raw, unformatted text.")
        self.assertEqual(node.to_html(), "This is just raw, unformatted text.")

    def test_to_html_missing_value_raises_error(self):
        # Verifies that an exception is thrown if value is missing
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr_output(self):
        node = LeafNode("span", "Text piece", {"class": "bolded"})
        expected = "LeafNode(span, Text piece, {'class': 'bolded'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()