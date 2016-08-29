import shutil
import os

source_files = "C:\Users\James Clavelli\Desktop\A"
destination_files = "C:\Users\James Clavelli\Desktop\B"
            

def move_files():
    for files in os.listdir(source_files):
        shutil.move(source_files, destination_files)
        

move_files()
