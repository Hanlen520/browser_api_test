#!/usr/bin/env python
# coding:utf-8

import unittest
import requests
import hashlib
import os, sys
import datetime

def md5sum(fname):
    with open(fname, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


def download_apk(url):
    r = requests.get(url, stream=True)
    fname = r.url.split('/')[-1]
    with open(fname, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return fname


def compare_md5():
    config_url = ''
    j = requests.get(config_url).json()
    for pkg in j['rtpkgs']['list']:
        start_time = datetime.datetime.now().replace(microsecond=0)
        pkg_name = download_apk(pkg['url'])
        end_time = datetime.datetime.now().replace(microsecond=0)
        print(start_time - end_time)
        pkg_md5 = md5sum(os.getcwd() + os.path.sep + pkg_name)
        config_md5 = pkg['md5'].lower()
        if pkg_md5 != config_md5:
            print("Wrong MD5 packages: " + pkg['pkg'])


compare_md5()
