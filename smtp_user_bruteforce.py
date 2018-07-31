#!/usr/bin/python

#importing modules
import socket
import sys

if len(sys.argv) <=2:
    print ("Usage :"+ sys.argv[0] +" <username> <ip_addres>")
    sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
connect = s.connect((sys.argv[2],25)) #connect to the server
banner = s.recv(1024)                     #Receive the banner
print (banner)
s.send('VRFY ' + sys.argv[1] +'\r\n')       #VRFY a user
result = s.recv(1024)
print result
s.close()                                 #close the socket
