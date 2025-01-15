from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if len(block) > 0:
            new_blocks.append(block.strip())
    return new_blocks

def block_to_block_type(block):
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    
    block_lines = block.split("\n")
    quote = all(line.startswith(">") for line in block_lines)
    if quote:
        return block_type_quote
    
    unordered_list = all(line.startswith("* ") or line.startswith("- ")
                         for line in block_lines)
    if unordered_list:
        return block_type_ulist
    
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate( block_lines)):
        return block_type_olist
    else:
        return block_type_paragraph

def markdown_to_html_node(text):
    blocks = markdown_to_blocks(text)
    div_node = ParentNode("div", children=[])

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == block_type_paragraph:
            html_node = ParentNode("p",children=[])
        elif block_type == block_type_heading:
            head = block.split(" ", 1)
            head_tag = heading_type(head[0])
            html_node = ParentNode(head_tag, children=[])
        elif block_type == block_type_quote:
            html_node = ParentNode("blockquote", children=[])
        elif block_type == block_type_ulist:
            html_node = ParentNode("ul", children=[])
        elif block_type == block_type_olist:
            html_node = ParentNode("ol", children=[])
        elif block_type == block_type_code:
            html_node = ParentNode("code", children=[])

        
        if block_type in (block_type_ulist, block_type_olist):
            list_items = block.split("\n")
            html_children = []
            
            for item in list_items:
                content = item.split(" ", 1)
                if len(content) > 1:
                    leaf_node = LeafNode("li", content[1], None)
                    html_children.append(leaf_node)

            html_node.children = html_children
            div_node.children.append(html_node)
        elif block_type is block_type_heading:
            body = head[1]
            html_children = text_to_children(body)
            html_node.children = html_children
            div_node.children.append(html_node)
        else:
            html_children = text_to_children(block)
            html_node.children = html_children
            div_node.children.append(html_node)
        
        
    return div_node

def heading_type(text):

    count = text.count("#")
    if 1 <= count <= 6:
        return f"h{count}"
    else:
        raise ValueError("Invalid heading level")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children_nodes = []
    for node in text_nodes:
        children_nodes.append(text_node_to_html_node(node))

    return children_nodes

markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
#print()
markdown_to_html_node(markdown)