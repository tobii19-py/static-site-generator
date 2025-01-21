import os
from block_markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")

    with open (from_path) as src_file:
        source = src_file.read()
        src_file.close()

    with open(template_path) as temp_file:
        template = temp_file.read()
        temp_file.close()

    node = markdown_to_html_node(source)
    content = node.to_html()
    title = extract_title(source)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
        
    with open(dest_path, "w") as page_file:
        page_file.write(page)
        page_file.close()
   