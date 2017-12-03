#!/usr/bin/env python
# coding:utf-8

import unittest
import requests
import hashlib
import os


def md5sum(fname):
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else:
            fh.seek(0)

    m = hashlib.md5()
    if isinstance(fname, str) and os.path.exists(fname):
        with open(fname, 'rb') as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    elif fname.__class__.__name__ in ['StringIO', "StringO"] or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()


def download_apk(apk_url):
    resp = requests.get(apk_url, stream=True)
    apk_fname = resp.url.split('/', -1)[-1]
    f = open(apk_fname, 'wb')
    for chunk in resp.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
    return apk_fname


def compare_md5():
    config_url = ''
    j = requests.get(config_url).json()
    for pkg in j['rtpkgs']['list']:
        pkg_name = download_apk(pkg['url'])
        pkg_md5 = md5sum(pkg_name)
        config_md5 = pkg['md5']
        if pkg_md5 != config_md5:
            print(pkg['pkg'])


compare_md5()
