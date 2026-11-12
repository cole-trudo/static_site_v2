from textnode import TextNode,TextType
from CopyStatic import CopyStaticFiles
import shutil
import os
from generate_pages_recursive import generate_pages_recursive
import sys
def main():
    public_dir="./public"
    docs_dir="./docs"

    if len(sys.argv)==2:
        basepath= sys.argv[1]
    else:
        basepath="/"


    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.mkdir(docs_dir)
    
    CopyStaticFiles("./static",docs_dir)
    generate_pages_recursive("content","template.html",docs_dir,basepath)

if __name__=='__main__':
    main()