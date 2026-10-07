class HTMLNode:
    def __init__(self,tag:str=None,value:str=None,children:list=None,props:dict=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props is None or self.props=={}:
            return ""
        else:
            f_string=""
            for key, value in self.props.items():
                f_string+=f' {key}="{value}"'
            return f_string
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None , value=None,children=None, props = None):
        super().__init__(tag, value, children, props)
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            return(f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag womp")
        if self.children is None:
            raise ValueError(" no kids  ERROR!!!")
        else:
            children_html=""
            for child in self.children:
                children_html+= child.to_html()
            
            return(f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>')


        
        
    