import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        # tag, value, children, props
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://somedomain.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://somedomain.com"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I don't understand",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I don't understand",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "Where is Batman",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Where is Batman, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()