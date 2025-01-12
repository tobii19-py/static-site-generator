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
