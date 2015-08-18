#!/usr/bin/python
#coding= utf-8
import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
time.sleep(5)
ssh.connect("192.168.29.188",22,"cotyb","111111")
stdin,stdout,stderr=ssh.exec_command("ls")
print stdout.readlines()
ssh.close
