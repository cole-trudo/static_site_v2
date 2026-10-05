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
        print(self.tag,self.value,self.children,self.props)
    