#!/bin/bash
chmod 777 nginx_log0    
chmod 777 nginx_log1   
chmod 777 nginx_log2    
chmod 777 nginx_log3    
chmod 777 nginx_log4    
chmod 777 nginx_log5    
while :
do 
    python server_number.py
done
