#import matplotlib
#matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy
import time
import random
import paramiko
import threading
import os


ip_list = ['10.1.2.3','10.1.2.4','10.1.2.5','10.1.2.6','10.1.2.7','10.1.2.8']
keylist = []
valuelist = []
textlist = []
barlist = []
barwidth=0.5
red,green,blue = 0,0,0
color = '#'+str(red)+str(green)+str(blue)
maxHeight = 5000

result = [1,1,1,1,1,1]
out = [0,0,0,0,0,0]

cmd = 'wc -l < /var/log/nginx/access.log'
cmd_clean = ['chmod 777 /var/log/nginx/access.log','cat /dev/null > /var/log/nginx/access.log']
username = "server1"
passwd = "123456"

for i in range(1,7):
	keylist.append("server"+str(i))
#for i in range(1,7):
#	filename = 'data'+str(i)+'.log'
#	item = open(filename, 'r')
#	for count,line in enumerate(item):  
#	    pass  
#	valuelist.append(count+1)
#	count = 0
#	item.close()
#print valuelist

def clean_log():
    count = 10
    print "waitng... clean the logs..."
    while count >= 0:
        for i in range(6):
	#ip = '192.168.29.188'	    
	    ip = ip_list[i]
	    a = threading.Thread(target = ssh3, args = (ip,username,passwd,cmd,i))
	    a.start()
	    count = count - 1
	    time.sleep(0.2)
	time.sleep(1)	#waiting to process
	#return result

def getAccessCount():
	for i in range(6):
		#ip = '192.168.29.188'	    
	 	ip = ip_list[i]
		a = threading.Thread(target = ssh2, args = (ip,username,passwd,cmd,i))
		a.start()

	time.sleep(0.5)	#waiting to process
	#return result

def ssh3(ip,username,passwd,cmd,i):
    try:
        ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,22,username,passwd,timeout=5)
	for m in cmd_clean:
	    stdin,stdout,stderr = ssh.exec_command(m)
	#result[i] = stdout.readInt()
        #out[i] = stdout.readlines()
	#print "out["+str(i)+"]:"+str(out[i])
	#result[i] = int(out[i][0])
	#print "result["+str(i)+"]:"+str(result[i])

	ssh.close()
    except:
	print '%s\tError\n'%(ip)
	#print "out["+str(i)+"]:"+str(out[i])
	#print "result["+str(i)+"]:"+str(result[i])

def ssh2(ip,username,passwd,cmd,i):
    try:
        ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,22,username,passwd,timeout=5)
	
	stdin,stdout,stderr = ssh.exec_command(cmd)
	#result[i] = stdout.readInt()
        out[i] = stdout.readlines()
	#print "out["+str(i)+"]:"+str(out[i])
	result[i] = int(out[i][0]) + 1
	print "result["+str(i)+"]:"+str(result[i])

	ssh.close()
    except:
	print '%s\tError\n'%(ip)
	#print "out["+str(i)+"]:"+str(out[i])
	#print "result["+str(i)+"]:"+str(result[i])


def animated_barplot():
	global valuelist
	for i in range(0,6):
		barlist.append(plt.bar(i+0.5,valuelist[i],width=barwidth,color='#00FF00'))
	for i in range(0,6):
		textlist.append(plt.text(i+0.68,valuelist[i]+50 ,str(valuelist[i])))
	while True:
		#for i,x in enumerate(valuelist):
		#	valuelist[i] = x + random.randint(1,50)
		#print valuelist
		
		getAccessCount()
		valuelist = result[:]
        	for i,bar in enumerate(barlist):
			bar[0].set_height(valuelist[i])
			red = hex(int(float(valuelist[i])/maxHeight*256)).zfill(2)[2:]
			green = hex(int(float(1-float(valuelist[i])/maxHeight)*256)).zfill(2)[2:]
			if red=='100':
				red = 'FF'
			if green=='100':
				green = 'FF'
			color = '#'+str(red).zfill(2)+str(green).zfill(2)+"00"
			bar[0].set_color(color)

        	for i,text in enumerate(textlist):
			text.set_position([i+0.68,valuelist[i]+50])
			text.set_text(str(valuelist[i]))

	        fig.canvas.draw()
		time.sleep(0.2)		#check interval

if __name__ == '__main__':
	clean_log()
	print "clean done!"
	getAccessCount()
	valuelist = result[:]

	print "valuelist1:"+str(valuelist)

	fig = plt.figure(figsize=(20.0, 10.0))
	plt.xlabel('server cluster',size=20)
	plt.ylabel('access count',size=20)
	plt.title(u'loadbalance statistic',size=30)
	plt.axis([0, 6.5, 0, maxHeight])
	xVal=numpy.arange(len(keylist))
	plt.xticks(xVal+barwidth+0.25,keylist)
	win = fig.canvas.manager.window
	#win.set_title("loadbalance hist")
	win.after(10, animated_barplot)
	plt.show()
