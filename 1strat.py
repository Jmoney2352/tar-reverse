import socket
import os

os.system("cls && title Server")

ip = "127.0.0.1"
port = 50000

s = socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
s.bind((ip, port))
s.listen()

c, addr = s.accept()

print(addr, " - Has Connected")
