from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    textnode_list = []

    for node_item in old_nodes:
        if node_item.text_type == TextType.NORMAL:
            node_objects = node_item.text.split(delimiter)

            for obj, part in enumerate(node_objects):
                if obj % 2 == 1:
                    textnode_list.append(TextNode(part, text_type))
                else:
                    textnode_list.append(TextNode(part, node_item.text_type))
        
        else:
            # If not normal text, append to textnode list as-is
            textnode_list.append(node_item)
    
    return textnode_list

def extract_markdown_images(text):
    matched_alts = re.findall(r"\[(.*?)\]", text)
    matched_urls = re.findall(r"\((.*?)\)", text)

    md_imgs = []

    for i in range(len(matched_alts)):
        md_imgs.append((matched_alts[i], matched_urls[i]))

    return md_imgs

def extract_markdown_links(text):
    matched_anchors = re.findall(r"\[(.*?)\]", text)
    matched_urls = re.findall(r"\((.*?)\)", text)

    md_links = []

    for i in range(len(matched_anchors)):
        md_links.append((matched_anchors[i], matched_urls[i]))

    return md_links
