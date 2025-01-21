import os
import shutil
from block_markdown import markdown_to_html_node
from htmlnode import ParentNode

def generate_page(from_path, template_path, dest_path):
    print("==============================================================================")
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")
    print("==============================================================================")

    with open (from_path) as src_file:
        source = src_file.read()
        src_file.close()

    with open(template_path) as temp_file:
        template = temp_file.read()
        temp_file.close()

    print(template)

    node = markdown_to_html_node(source)
    print(node)
    