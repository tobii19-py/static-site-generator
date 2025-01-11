from md_to_textnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image
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

    def test_ext_md_imgs(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_ext_md_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        )

    def test_spltnd_imgs(self):
        node = TextNode(
            "This is text with an image of boots ![boots](https://www.boot.dev) and the goat ![kenpachi zaraki](https://static0.gamerantimages.com)",
            TextType.NORMAL,
        )
        result = [
            TextNode("This is text with an image of boots ", TextType.NORMAL),
            TextNode("boots", TextType.IMAGES, "https://www.boot.dev"),
            TextNode(" and the goat ", TextType.NORMAL),     
            TextNode("kenpachi zaraki", TextType.IMAGES, "https://static0.gamerantimages.com")
        ]
        self.assertEqual(split_nodes_image([node]), result)

