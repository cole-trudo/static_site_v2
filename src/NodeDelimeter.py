from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    #looks for markdown notes for each of our types.it only does plain bold italic and code for rn. 
    # so it should take a PLAIN type, then be able to handle a nested code 
    node_list=[]
    for node in old_nodes:
        if node.text_type!=TextType.PLAIN:
            node_list.append(node)
            continue
        
        codeset=node.text.split(delimiter)
        if len(codeset)%2==0:
            raise ValueError("Missing closing delimeter... check data")
        for i,item in enumerate(codeset):
            if item=="":
                continue
            if i%2==0:
                node_list.append(TextNode(item,TextType.PLAIN))
            else:
                node_list.append(TextNode(item, text_type))
        
    return node_list
    







    