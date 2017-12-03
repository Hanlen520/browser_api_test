# urs/bin/python
# encoding:utf-8
import os
import re
import shutil

path = os.getcwd()


def get_dest_name(apk):
    pattern = re.compile(r'\w+_(\w+)\.apk')
    match = pattern.match(apk)
    if match:
        dest_name = "360_chromium_" + match.group(1) + ".apk"
    else:
        print("please check the apk name:" + apk)
    return dest_name


dest_dir = path + '/renamed'
dest_dir = path + os.path.sep + "renamed"
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
raw_apks = os.listdir(path)
for raw_apk in raw_apks:
    if raw_apk.endswith('.apk'):
        dest_name = get_dest_name(raw_apk)
        shutil.copyfile(path + os.path.sep + raw_apk, dest_dir + os.path.sep + dest_name)
