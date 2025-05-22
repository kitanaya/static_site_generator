import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is one text node", TextType.ITALIC)
        node2 = TextNode("This is a second text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("TextNode", TextType.CODE, "https://domain.tld")
        node2 = TextNode("TextNode", TextType.CODE, None)
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("TextNode", TextType.LINKS)
        node2 = TextNode("TextNode", TextType.IMAGES)
        self.assertNotEqual(node, node2)

    def test_eq_type(self):
        node = TextNode("TextNode", TextType.BOLD)
        self.assertIsInstance(node, TextNode)


if __name__ == "__main__":
    unittest.main()
