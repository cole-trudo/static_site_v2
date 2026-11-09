from textnode import TextNode,TextType
from CopyStatic import CopyStaticFiles
import shutil
import os
from generate_page import generate_page
def main():
    public_dir="./public"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    
    CopyStaticFiles("./static","./public")
    generate_page("content/index.md","template.html","public/index.html")

if __name__=='__main__':
    main()