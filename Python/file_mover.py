import shutil
import os
            
def move_files(src_path, dst_path):
    for files in os.listdir(src_path):
        if files.endswith(".txt"):
            src_file = os.path.join(src_path, files)
            dst_file = os.path.join(dst_path, files)
            shutil.move(src_file, dst_path)
            print("\nFile: {}\nMoved to: {}".format(files, dst_file))
        
        
if __name__ == '__main__':
    src_path = "C:\Users\James Clavelli\Desktop\A"
    dst_path = "C:\Users\James Clavelli\Desktop\B"
    
    move_files(src_path,dst_path)
