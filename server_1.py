from socket import *
from threading import *
from time import *
from select import *

#aaaaaaa

# counter = 0
# def func(c, addr):
#     global counter
#     a = int(c.recv(3).decode())
#     b = int(c.recv(3).decode())
#     sleep(40)
#     c.sendall(str(a + b).encode())
#     counter -= 1
#
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('127.0.0.1', 12345))
# s.listen()
#
# while True:
#     c, addr = s.accept()
#     counter += 1
#     if (counter > 4):
#         print("rejected!")
#         counter -= 1
#         c.sendall("Server Is Busy".encode())
#     else:
#         print("accepted :",addr,counter)
#         Thread(target=func, args=(c, addr)).start()
# s.close()


#bbbbb
# counter = 0
# def func(c, addr):
#     global counter
#     a = int(c.recv(3).decode())
#     b = int(c.recv(3).decode())
#     c.sendall(str(a + b).encode())
#     counter -= 1
#
# s = socket(AF_INET6, SOCK_STREAM)
# s.bind(('::1', 12345))
# s.listen()
#
# while True:
#     c, addr = s.accept()
#     counter += 1
#     if (counter > 4):
#         print("rejected!")
#         counter -= 1
#         c.sendall("Server Is Busy".encode())
#     else:
#         print("accepted :",addr,counter)
#         Thread(target=func, args=(c, addr)).start()
# s.close()

#ccccc
# def func(c, addr):
#     global counter
#     a = int(c.recv(3).decode())
#     b = int(c.recv(3).decode())
#     c.sendall(str(a + b).encode())
#     counter -= 1
#
# counter = 0
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('127.0.0.1', 12345))
# ss = socket(AF_INET, SOCK_STREAM)
# ss.bind(('127.0.0.1', 12346))
# s.listen()
# ss.listen()
# ls = [s,ss]
#
# while True:
#     r,w,e=select(ls,[],ls)
#     for i in r:
#         c, addr = i.accept()
#         counter += 1
#         if (counter > 4):
#             counter -= 1
#             c.sendall("Server Is Busy".encode())
#         else:
#             print("accepted :", addr, counter)
#             Thread(target=func, args=(c, addr)).start()
# s.close()
#ddddd

counter = 0
def func(c, addr):

    global counter
    c.settimeout(5.0)
    try:
        a = int(c.recv(3).decode())
        b = int(c.recv(3).decode())
        c.sendall(str(a + b).encode())
        counter -= 1
    except timeout:
        print('time out reached')
        counter -= 1
        c.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen()

while True:
    c, addr = s.accept()
    counter += 1
    if (counter > 4):
        print("rejected!")
        counter -= 1
        c.sendall("Server Is Busy".encode())
    else:
        print("accepted :",addr,counter)
        Thread(target=func, args=(c, addr)).start()
s.close()



