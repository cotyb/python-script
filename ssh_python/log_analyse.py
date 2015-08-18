#!/usr/bin/python
import os
import paramiko
import time
t = paramiko.Transport(("192.168.29.188",22))
t.connect(username="cotyb",password="111111")
sftp = paramiko.SFTPClient.from_transport(t)
#remotepath = '/home/cotyb/chen.txt'
homedir = os.getcwd()
remotepath = '/var/log/nginx/access.log'
localpath = homedir + '/nginx.log'
#sftp.put(localpath,remotepath)

sftp.get(remotepath,localpath)
fd = os.open('/home/cotyb/Desktop/nginx.log',os.O_RDWR)
#os.chdir('/home/cotyb/Desktop')
os.fchmod(fd,os.O_RDWR)
#time.sleep(1)
t.close()
