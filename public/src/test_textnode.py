import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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
        node = TextNode("TextNode", TextType.LINK)
        node2 = TextNode("TextNode", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_eq_type(self):
        node = TextNode("TextNode", TextType.BOLD)
        self.assertIsInstance(node, TextNode)


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node with **BOLD** text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node with **BOLD** text")
    
    def test_italic(self):
        node = TextNode("This is a text node with *italic* text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node with *italic* text")

    def test_code(self):
        node = TextNode("This is a text node with `code` text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node with `code` text")

    def test_link(self):
        node = TextNode("This is a text node with a LINK", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node with a LINK")
        self.assertEqual(html_node.props, {"href": "https://google.com"})

    def test_image(self):
        node = TextNode("This is a text node with an IMAGE", TextType.IMAGE, "path_to_image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "path_to_image", "alt": "This is a text node with an IMAGE"})

if __name__ == "__main__":
    unittest.main()
