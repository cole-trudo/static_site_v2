from textnode import TextNode,TextType
from CopyStatic import CopyStaticFiles
import shutil
import os
def main():
    public_dir="./public"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    
    CopyStaticFiles("./static","./public")
if __name__=='__main__':
    main()