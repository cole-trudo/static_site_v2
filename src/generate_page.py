from markdown_to_html_node import markdown_to_html_node
from htmlnode import ParentNode,LeafNode
from extractTitle import extract_title
import os

def generate_page(from_path, template_path, dest_path,basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    f=open(from_path)

    from_contents=f.read()
    f.close()

    t=open(template_path)

    template_contents=t.read()

    t.close()

    FromNode= markdown_to_html_node(from_contents).to_html()
    title=extract_title(from_contents)

    titledTemplate=template_contents.replace('{{ Title }}',title)
    updateTemplate=titledTemplate.replace("{{ Content }}", FromNode)
    hrefTemplate=updateTemplate.replace('href="/', f'href="{basepath}')
    updateWithSrc=hrefTemplate.replace('src="/', f'src="{basepath}')



    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    f=open(dest_path,mode='w')
    f.write(updateWithSrc)
    f.close()
    
    






    
    






