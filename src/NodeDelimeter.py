from textnode import TextNode, TextType, extract_markdown_images, extract_markdown_links


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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    node_list=[]
    for node in old_nodes:
        if node.text_type!=TextType.PLAIN:
            node_list.append(node)
            continue
        splitPoint=extract_markdown_images(node.text)
        theRest=node.text
        for Point in splitPoint:
            altTxt,image=Point
            before,after=theRest.split(f"![{altTxt}]({image})",1)
            if before!="":
                node_list.append(TextNode(before,TextType.PLAIN))
            node_list.append(TextNode(altTxt,TextType.IMAGE,image))
            theRest=after
        if theRest!="":
            node_list.append(TextNode(theRest,TextType.PLAIN))
    return node_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    node_list=[]
    for node in old_nodes:
        if node.text_type!=TextType.PLAIN:
            node_list.append(node)
            continue
        splitPoint=extract_markdown_links(node.text)
        theRest=node.text
        for Point in splitPoint:
            hypertxt,link=Point
            before,after=theRest.split(f"[{hypertxt}]({link})",1)
            if before!="":
                node_list.append(TextNode(before,TextType.PLAIN))
            node_list.append(TextNode(hypertxt,TextType.LINK,link))
            theRest=after
        if theRest!="":
            node_list.append(TextNode(theRest,TextType.PLAIN))
    return node_list



      

     
            

    
    







    