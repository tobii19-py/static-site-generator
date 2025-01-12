from md_to_textnode import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_image, 
    split_nodes_link,
    text_to_textnodes,
)
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

    def test_splnd_lnks(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        result = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(split_nodes_link([node]), result)

    def test_txtto_txtnds(self):
        text= "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), result)

    def test_multi_imgs_txtnds(self):
        text = "This might be **you wouldn't get it** ![Joker](https://knowyourmeme.com/memes/you-wouldnt-get-it) and ![Tony Stark](https://makeameme.org/meme/you-wouldnt-get-af2cb9e3c0)"
        result = [
            TextNode("This might be ", TextType.NORMAL),
            TextNode("you wouldn't get it", TextType.BOLD),
            TextNode(" ", TextType.NORMAL),
            TextNode("Joker", TextType.IMAGES, "https://knowyourmeme.com/memes/you-wouldnt-get-it"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("Tony Stark", TextType.IMAGES, "https://makeameme.org/meme/you-wouldnt-get-af2cb9e3c0"),
        ]
        self.assertEqual(text_to_textnodes(text), result)

    def test_multi_code_txtnds(self):
        text = "This is definitely `code` and another `poorly written code`"
        result = [
            TextNode("This is definitely ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" and another ", TextType.NORMAL),
            TextNode("poorly written code", TextType.CODE),
            TextNode("", TextType.NORMAL)
        ]
        self.assertEqual(text_to_textnodes(text), result)
