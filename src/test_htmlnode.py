import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = HTMLNode("a", "This is a text for HTML node", 
                        [], {"href":"https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_2(self):
        node = HTMLNode("p", "This is another text for HTML node", 
                        ["h1"], {"href": "https://www.youtube.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.youtube.com\" target=\"_blank\"")
    
    def test_3(self):
        node = HTMLNode("h1", "This is a third text for HTML node", 
                        [], {"href": "https://www.yahoo.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.yahoo.com\" target=\"_blank\"")

    def test_4(self):
        node = LeafNode("p", "just text", {})
        self.assertEqual(node.to_html(), "<p>just text</p>")
    
    def test_5(self):
        node = LeafNode("div", "hello", {"class": "big", "id": "greeting"})
        self.assertEqual(node.to_html(), '<div class="big" id="greeting">hello</div>')

    def test6(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
                        node.to_html(), 
                        "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
                        )

    
if __name__ == "__main__":
    unittest.main()