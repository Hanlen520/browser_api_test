import os
import shutil


def get_file_name(file):
    return os.path.splitext(file)[0] + os.path.splitext(file)[1].upper()


path = os.getcwd() + os.path.sep + 'files'
dest_dir = os.path.dirname(os.getcwd()) + os.path.sep + 'renamed'
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

raw_files = os.listdir(path)
for raw_file in raw_files:
    dest_file = get_file_name(raw_file)
    print(dest_file)
    print(path + os.path.sep + raw_file)
    print(dest_dir + os.path.sep + dest_file)
    shutil.copyfile(path + os.path.sep + raw_file, dest_dir + os.path.sep + dest_file)
