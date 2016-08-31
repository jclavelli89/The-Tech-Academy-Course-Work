import os, os.path, schedule, shutil, time
import datetime as dt
from datetime import date,  datetime, timedelta



def daily_copy_script(src_path, dst_path):
    for files in os.listdir(src_path):
        if files.endswith(".txt") and mtime > ago:
            src_file = os.path.join(src_path, files)
            dst_file = os.path.join(dst_path, files)
            shutil.move(src_file, dst_path)
            print("\nFile: {}\nmoved to: {}".format(files, dst_file))




if __name__ == '__main__':
    src_path = "C:\Users\James Clavelli\Desktop\A"
    dst_path = "C:\Users\James Clavelli\Desktop\B"
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
    st = os.stat(src_path)
    mtime = dt.datetime.fromtimestamp(st.st_mtime)
    
    daily_copy_script(src_path,dst_path)





"""
utilizing os.stat, we want to add to file_mover a timer utilizing datetime .now
with > or < symbols and using the read out of a condition provided by os.stat
related to the new files. In addition, files will need to be copied, not moved
and the folder will need me to creaet new files to really work it. Should be able to
compelte this in the 10 - 12 hour this evening

"""

