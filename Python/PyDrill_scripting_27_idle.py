import os, os.path, shutil, time


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

if __name__ == '__main__':
    src_path = "C:\Users\James Clavelli\Desktop\A"
    dst_path = "C:\Users\James Clavelli\Desktop\B"
    daily_copy_script(src_path,dst_path)


