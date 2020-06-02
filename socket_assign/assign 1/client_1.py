from socket import *
from time import *


s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 12345))
# s = socket(AF_INET6, SOCK_STREAM)
# s.connect(("::1", 12345))
sleep(20)
s.sendall('001'.encode())
s.sendall('002'.encode())
temp = s.recv(1024).decode()
print("server answer :",temp)
s.close()