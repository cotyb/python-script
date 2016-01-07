#! /bin/bash
#
# Program:
#	Usage: InstallJDK <source files>
#
#	This program can help you install Java rapidly
#	and help configure relevant settings.
# History:
# 2014/7/30   Li Yunpeng  First  release
# 2014/7/31   Li Yunpeng  Second release   Add "Version matching"
# 2014/8/1    Li Yunpeng  Third  release   Add support "*.bin"


#Exclude other documents.

if
  echo $1 | sed 's/^.*\.//g'| grep -Ev 'bin|gz' > /dev/null
then
  echo "This program only can be used to install *.tar.gz or *.bin file."
  exit 1
fi

#Version matching
if
  echo $1 | grep "x64" > /dev/null
  uname -a | grep -v "x86_64" > /dev/null
then
	echo "Error 1 ! Version Mismatch !"
	exit 1
elif
  [[ $(echo $1 | grep "i586") && \
     $(uname -a | grep "x86_64") ]]
then
	echo "Error 2 ! Version Mismatch !"
	exit 1
fi

#check up if log in by root
if [ `whoami` != "root" ];then
	echo "Please use this command in root."
	exit 1
fi

ls > /tmp/InstallJavaCatalog.old
#Decompressing files
if  # Different packages use different way to unzip
  echo $1 | sed 's/^.*\.//g'| grep "gz" > /dev/null
then
  tar zxvf "$1"
else
  ./$1
fi

ls> /tmp/InstallJavaCatalog.new
#Get the folder's name of Java
Filename=`diff /tmp/InstallJavaCatalog.old /tmp/InstallJavaCatalog.new | grep "^>" |tr -d '> '`

#Delete temporary files
rm -f /tmp/InstallJavaCatalog.old
rm -f /tmp/InstallJavaCatalog.new

#Found the folder
mkdir -p /usr/lib/jvm/
#Move Java's folder to /usr/lib/jvm/
mv -i $Filename /usr/lib/jvm/

echo "Configuring relevant settings"
#Add the environment variable
echo  "JAVA_HOME=/usr/lib/jvm/$Filename" >> /etc/profile
echo  'PATH=$JAVA_HOME/bin:$PATH
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export JAVA_HOME
export PATH
export CLASSPATH' >> /etc/profile
#source /etc/profile

echo "--------------------------------------"
echo "Installation has been completed."
echo "Please logoff."
echo "--------------------------------------"
