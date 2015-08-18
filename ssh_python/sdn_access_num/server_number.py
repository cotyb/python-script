#!/usr/bin/python
import os
list = [0,0,0,0,0,0]
nowdir = os.getcwd()
for i in range(6):
    list[i] = len(open(nowdir + "/nginx_log" + str(i),'r').readlines())
    print list[i]
