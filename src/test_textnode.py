import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_with_url(self):
        node = TextNode("Link node", TextType.LINK,"https://www.boot.dev")
        node2 = TextNode("Link node", TextType.LINK,"https://www.boot.dev")
        self.assertEqual(node,node2)
    def test_not_eq_text_type(self):
        node = TextNode("This is text",TextType.BOLD)
        node2 = TextNode("This is text",TextType.ITALIC)
        self.assertNotEqual(node,node2)
    def test_not_eq_url(self):
        node = TextNode("Link node", TextType.LINK, "https://www.goole.com")
        node2 = TextNode("Link node",TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node,node2)
    def test_repr(self):
        node = TextNode("Text", TextType.CODE)
        self.assertEqual(repr(node),"TextNode(Text,code,None)")


if __name__ == "__main__":
    unittest.main()