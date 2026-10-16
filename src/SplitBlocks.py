from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="qoute"
    UNORDERED_LIST="unordered_list"
    ORDERED_LIST="ordered_list"



def block_to_block_type(block):
    if re.match(r"^#{1,6} .+", block):
        return BlockType.HEADING
    if re.match(r"^```\n.*```$", block, re.DOTALL):
        return BlockType.CODE
    if re.match(r"^>.*(\n>.*)*$", block):
        return BlockType.QUOTE
    if re.match(r"^- .*(\n- .*)*$", block):
        return BlockType.UNORDERED_LIST
    if re.match(r"^\d+\. .*(\n\d+\. .*)*$", block):
        lines = block.split("\n")
        if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, 1)):
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

    







def markdown_to_blocks(markdown):

    fresh_set=[]

    

    header=markdown.split("\n\n")
    
    for item in header:
        newboy=item.strip()
        if newboy!="":
            fresh_set.append(newboy)
        

    return(fresh_set)



    

