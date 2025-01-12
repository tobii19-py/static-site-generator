def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if len(block) > 0:
            new_blocks.append(block.strip())
    return new_blocks

def block_to_block_type(block):
    if block.startswith("#", 0, 5):
        return f"'{block}' type is Heading"
    if block.startswith("```") and block.endswith("```"):
        return f"'{block}' type is Code"
    
    block_lines = block.split("\n")
    quote = all(line.startswith(">") for line in block_lines)
    if quote:
        return f"'{block}' type is Quote"
    
    unordered_list = all(line.startswith("* ") or line.startswith("- ")
                         for line in block_lines)
    if unordered_list:
        return f"'{block}' type is Unordered List"
    
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate( block_lines)):
        return f"'{block}' type is Ordered List"
    else:
        return f"'{block}' is a regular paragraph"
