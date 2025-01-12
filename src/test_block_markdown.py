from block_markdown import markdown_to_blocks, block_to_block_type
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
        
        self.assertEqual(block_to_block_type(blocks[0]), 
                         f"'{blocks[0]}' type is Heading")
        
        self.assertEqual(block_to_block_type(blocks[1]),
                         f"'{blocks[1]}' is a regular paragraph")
        
        self.assertEqual(block_to_block_type(blocks[2]),
                         f"'{blocks[2]}' type is Unordered List")
        
    def test_ordered_lists(self):
        markdown = """
1. This is first
2. Second item
3. Third item
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),
                         f"'{blocks[0]}' type is Ordered List")


