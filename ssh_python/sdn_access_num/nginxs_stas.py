#!/usr/bin/python
import os
import paramiko
import time
ilist=["10.1.2.3","10.1.2.4","10.1.2.5","10.1.2.6","10.1.2.7","10.1.2.8"]
remotepath = '/var/log/nginx/access.log'
homedir = os.getcwd()
while 1:
    for i in range(6):
        t = paramiko.Transport(("192.168.29.188",22))
        t.connect(username="cotyb",password="111111")
        sftp = paramiko.SFTPClient.from_transport(t)
        localpath = homedir + '/nginx_log'+ str(i)
        sftp.get(remotepath,localpath)
       # fd = os.open('/home/cotyb/Desktop/nginx.log'+ str(i),os.O_RDWR)
        #os.chdir('/home/cotyb/Desktop')
      #  os.fchmod(fd,os.O_RDWR)
    time.sleep(1)
t[i].close()
