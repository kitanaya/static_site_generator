import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_ahref(self):
        node = LeafNode("a", "Click here!", {"href" : "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click here!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello Friend")
        self.assertEqual(node.to_html(), "Hello Friend")

    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()