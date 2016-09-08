import os, os.path, shutil, time
from tkinter import * 
from tkinter import ttk

#You're going to create your code
# then attribute the code to a button with command= 

def daily_copy_script(src_path, dst_path):
    for files in os.listdir(src_path):
        if files.endswith(".txt"):
            src_file = os.path.join(src_path, files)
            dst_file = os.path.join(dst_path, files)
            fileMod = time.time() - (os.path.getmtime(src_file))
            _24hrsAgo = time.time() - (24 *60 *60)
            last24hrs = time.time() - _24hrsAgo
            if fileMod < last24hrs:
                shutil.copy(src_file, dst_path)
                print("\nFile: {}\ncopied to: {}".format(files, dst_file))

root = Tk()
root.title("File Mover Selector")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


#if __name__ == '__main__':
#    src_path = r"C:\Users\James Clavelli\Desktop\A"
#    dst_path = r"C:\Users\James Clavelli\Desktop\B"
#    daily_copy_script(src_path,dst_path)




        

