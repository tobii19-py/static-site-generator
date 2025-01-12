from block_markdown import (
    markdown_to_blocks, 
    block_to_block_type,
    block_type_heading,
    block_type_paragraph,
    block_type_code,
    block_type_quote,
    block_type_olist,
    block_type_ulist,
)
import unittest

class TestBlockMarkdown(unittest.TestCase):
    def test_mdn2_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(markdown_to_blocks(markdown), result)

    def test_mdn2_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        result = [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
        self.assertEqual(markdown_to_blocks(markdown), result)

    def test_unordered_lists(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(markdown)
        
        self.assertEqual(block_to_block_type(blocks[0]), block_type_heading)
        
        self.assertEqual(block_to_block_type(blocks[1]), block_type_paragraph)
        
        self.assertEqual(block_to_block_type(blocks[2]), block_type_ulist)
        
    def test_ordered_lists(self):
        markdown = """
1. This is first
2. Second item
3. Third item
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]), block_type_olist)


