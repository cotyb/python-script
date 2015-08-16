#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'smile_tina'

import sys
import codecs

files = open("C:\Users\cotyb\Desktop\wiki.zh.text.jian.txt","r+")
bw = open("C:\Users\cotyb\Desktop\wiki.zh.text.single.txt","r+")
line = files.readline().decode('utf-8')
while line:
    strs = line.replace('/','')
    strs = strs.replace(' ','')
    tmp = ""
    for index in range(len(strs)):
        tmp = tmp + strs[index] + " "
    print tmp
    bw.write(tmp.encode("utf-8"))
    bw.flush()
    line = files.readline().decode('utf-8')
bw.close()
files.close()
