from SplitBlocks import markdown_to_blocks,block_to_block_type,BlockType
from htmlnode import HTMLNode, ParentNode
from enum import Enum
from textnode import text_node_to_html_node,TextNode,TextType
from NodeDelimeter import text_to_textnodes

#converts markdown doc into a single parent html node with many children.
# so raw markdown gets converted into a bunch of nodes, and t
def markdown_to_html_node(markdown):
    bigList=[]
    blocks=markdown_to_blocks(markdown)
    for block in blocks:
        Block_Type=block_to_block_type(block)
        typeTag=html_tag_from_blockType(Block_Type,block)
        Stripped=BlockStripper(block, Block_Type)
        
        # below needs to change from returning the parent node to collectign thrmblock type
        match Block_Type:
            case BlockType.CODE:
                Html=text_node_to_html_node(TextNode(block.removeprefix("```\n").removesuffix("```"), TextType.PLAIN))
                Codetag=ParentNode("code", [Html])
                Pretag=ParentNode("pre", [Codetag])
                bigList.append(Pretag)

            case BlockType.HEADING:
                 bigList.append(ParentNode(typeTag, text_to_children(Stripped)))
            case BlockType.PARAGRAPH:
                bigList.append(ParentNode(typeTag,text_to_children(Stripped)))
            case BlockType.QUOTE:
                stripped_lines=BlockStripper(block, Block_Type)
                joined= " ".join(stripped_lines)
                children= text_to_children(joined)
                bigList.append( ParentNode(typeTag, children))
            case BlockType.ORDERED_LIST:
                ListLi=[]
                stripped_lines=BlockStripper(block,Block_Type)
                for line in stripped_lines:
                    ListLi.append(ParentNode("li",text_to_children(line)))
                bigList.append(ParentNode(typeTag,ListLi))
            case BlockType.UNORDERED_LIST:
                ListLi=[]
                stripped_lines=BlockStripper(block,Block_Type)
                for line in stripped_lines:
                    ListLi.append(ParentNode("li",text_to_children(line)))
                bigList.append(ParentNode(typeTag,ListLi))
    return ParentNode("div", bigList)

       

def html_tag_from_blockType(Block_Type: BlockType,block)->str:
    #should this just create the parent node? I think it should actually just create the tag
    match Block_Type:
        case BlockType.CODE:
            return  "code"
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.HEADING:
            split=block.split(" ",1)
            count=split[0].count("#")
            return f"h{count}"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case _:
            raise ValueError("unknown type")
def BlockStripper(block, blocktype: BlockType):
    match blocktype:
        case BlockType.HEADING:
            stripped=block.split(" ",1)
            return stripped[1]
        case BlockType.QUOTE:
            StringList=[]
            each_line=block.split("\n")

            for line in each_line:
                stripped=line.split(">",1)
                StringList.append(stripped[1].strip())

            return StringList
        case BlockType.UNORDERED_LIST:
            StringList=[]
            each_line=block.split("\n")
         
            for line in each_line:
                stripped=line.split("-",1)
                StringList.append(stripped[1].strip())
            return StringList
        case BlockType.ORDERED_LIST:
            StringList=[]

            each_line=block.split("\n")
            for line in each_line:
                stripped=line.split(". ",1)
                StringList.append(stripped[1].strip())
            return StringList
        case BlockType.PARAGRAPH:
            return block.replace("\n", " ")


    
def text_to_children(text):
    #convert raw text to a text node
    NodeList=[]
    NewNodes=text_to_textnodes(text)
    for node in NewNodes:
        NodeList.append(text_node_to_html_node(node))
    return NodeList

    


