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
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    image_nodes = []

    for node_item in old_nodes:
        if not node_item.text:
            continue
        
        images = extract_markdown_images(node_item.text)

        if not images:
            if node_item.text:
                image_nodes.append(node_item)
            continue
        else:
            img = images[0]
            alt = img[0]
            link = img[1]
            sections = node_item.text.split(f"![{alt}]({link})", 1)
            
            if sections[0]:
                image_nodes.append(TextNode(sections[0], TextType.NORMAL))
            if alt:
                image_nodes.append(TextNode(alt, TextType.IMAGES, link))
            if sections[1]:
                follow_nodes = split_nodes_image([TextNode(sections[1], TextType.NORMAL)])
                image_nodes.extend(follow_nodes)

    return image_nodes

def split_nodes_link(old_nodes):
    link_nodes = []

    for node_item in old_nodes:
        if not node_item.text:
            continue

        links = extract_markdown_links(node_item.text)

        if not links:
            if node_item.text:
                link_nodes.append(node_item)
            continue
        else:
            link = links[0]
            anchor = link[0]
            url = link[1]

            sections = node_item.text.split(f"[{anchor}]({url})", 1)

            if node_item.text:
                link_nodes.append(TextNode(sections[0], TextType.NORMAL))
            if anchor:
                link_nodes.append(TextNode(anchor, TextType.LINKS, url))
            if sections[1]:
                remaining_links = split_nodes_link([TextNode(sections[1], TextType.NORMAL)])
                link_nodes.extend(remaining_links)

    return link_nodes

def text_to_textnodes(text):

    nodes = [TextNode(text, TextType.NORMAL)]

    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)

    return nodes
