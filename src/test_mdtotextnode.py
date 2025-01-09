from md_to_textnode import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertAlmostEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ]
        )

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bolded phrase** in the middle",
                        TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.NORMAL),
            ]
        )

    def test_not_normal_delimiter(self):
        node = TextNode("`AI definitely wrote this piece of code`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [TextNode("`AI definitely wrote this piece of code`", TextType.CODE)]
        )