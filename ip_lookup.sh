#!/bin/bash

for name in $(cat subdomain.txt);do host $name.$1 |grep "has address" | cut -d " " -f 1,4 ; done | sort | uniq

#if [ -z "$1" ];then
#	echo "[*] Simple Zone transfer script"
#	echo "[*] Usage :$0 <domain name>"
#	exit 0
#fi

#for name in $(cat subdomain.txt);do
#	host $name.$1 | grep "has address" | cut -d " " -f 1,4
#done
