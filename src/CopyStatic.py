import shutil
import os



def CopyStaticFiles(source_dir,destination_dir):
    copiedList=[]
   
    Source_list=os.listdir(source_dir)
    for item in Source_list:
        full_source_path= os.path.join(source_dir, item)
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path,destination_dir)
            copiedList.append(full_source_path)

        if os.path.isdir(full_source_path):
            new_dir_path=os.path.join(destination_dir, item)
            os.mkdir(new_dir_path)
            CopyStaticFiles(full_source_path,new_dir_path)
    
 
