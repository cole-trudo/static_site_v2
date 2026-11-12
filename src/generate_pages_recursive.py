import os
import shutil
import pathlib
from generate_page import generate_page



def  generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):


        copiedList=[]
       
        Content_dir=os.listdir(dir_path_content)
        for item in Content_dir:
            full_source_path= os.path.join(dir_path_content, item)
            dest_path=os.path.join(dest_dir_path,item)
            if os.path.isfile(full_source_path):

                

                generate_page(full_source_path,template_path,pathlib.Path(dest_path).with_suffix(".html"),basepath)

            if os.path.isdir(full_source_path):
                 generate_pages_recursive(full_source_path, template_path, dest_path,basepath)

                 
                