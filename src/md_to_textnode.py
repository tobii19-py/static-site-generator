from textnode import TextNode, TextType

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
