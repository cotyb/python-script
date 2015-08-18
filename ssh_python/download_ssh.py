#!/usr/bin/python
import paramiko
t = paramiko.Transport(("192.168.29.188",22))
t.connect(username="cotyb",password="111111")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = '/home/cotyb/chen.txt'
localpath = '/home/cotyb/chen.txt'
#sftp.put(localpath,remotepath)
sftp.get(remotepath,localpath)
t.close()
