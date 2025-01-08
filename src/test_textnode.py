import unittest

from textnode import TextNode, text_node_to_html_node, TextType
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_norm(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This isa text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_normal_text_node(self):
        node = TextNode("This may or may not be another normal text", TextType.NORMAL)
        actual = text_node_to_html_node(node)
        expected = LeafNode(None, "This may or may not be another normal text")
        print(f"Actual: tag={actual.tag}, text={actual.value}, href={actual.props}")
        print(f"Expected: tag={expected.tag}, text={expected.value}, href={expected.props}")
        self.assertEqual(actual, expected)
    
    """def test_bold_text_node(self):
        node = LeafNode("bold", "This is categorically not bold")
        self.assertEqual(node.text_node_to_html(),
                         "<b>")"""


if __name__ == "__main__":
    unittest.main()