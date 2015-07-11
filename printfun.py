#!/usr/bin/python
name = open("xx.x","r")
new_data = open("yy.y","r+")
line = name.readline()
while line:
    new_data.write(line)
    if line[0:3] == 'def':
        line = line[0:-1]
        new_data.write("    print " + "\"" + "%s"  %line + "\"\n")
    line = name.readline()
	
name.close()
new_data.close()
