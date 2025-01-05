import unittest

from htmlnode import HTMLNode

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
    
if __name__ == "__main__":
    unittest.main()