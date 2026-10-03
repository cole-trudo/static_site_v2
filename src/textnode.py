from enum import Enum


class TextType(Enum):
    PLAIN="plain"
    BOLD="bold"
    ITALIC="italic"
    CODE="code"
    LINK="link"



class TextNode:
    #need to default url to none
    def __init__(self,text:str,text_type:TextType,url:str)->None:
        self.text=text
        self.text_type=text_type
        self.url=url
    def equality(self,other):
        if self.text.__eq__(other.text) and self.text_type.__eq__(other.text_type) and self.url.__eq__(other.TextNode.url):
            return True
        return False
    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type}, {self.url})")






    
    
