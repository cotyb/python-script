[ 仅适用于Debian系(如Debian、Ubuntu等)Linux操作系统平台 ]

-----------------------------------------------------
                 InstallJDK.sh
-----------------------------------------------------
说明：一键配置JDK环境，支持*.tar.gz和*.bin两种格式,运行前不可自行解压相应压缩包
运行参数格式: bash InstallJDK.sh <sources file>
示例：bash InstallJDK.sh jdk-7u65-linux-x64.tar.gz
运行完之后请注销或重启一次，也可在终端输入source /etc/profile


-----------------------------------------------------
                 InstallJacap.sh
-----------------------------------------------------
说明：一键配置JDK,libpcap,jpcap三个软件的环境,运行前不可自行解压相应压缩包
运行参数格式:(三个参数顺序依次JDK,libpcap,jpcap，两个参数顺序依次libpcap,jpcap) 
   <1>  bash InstallJacap.sh <sources file> <sources file> <sources file>
   <2>  bash InstallJacap.sh <sources file> <sources file> 
示例：
   <1>  bash InstallJacap.sh jdk-6u45-linux-x64.bin libpcap-1.6.1.tar.gz jpcap-0.7.tar.gz
   <2>  bash InstallJacap.sh libpcap-1.6.1.tar.gz jpcap-0.7.tar.gz

