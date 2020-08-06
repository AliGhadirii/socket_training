from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1",1234))
except error:
    print("Failed to run server!")
s.listen()
c, addr = s.accept()
try:
    while True:
        data = c.recv(10000).decode()
        print(data)
        if (data == "good bye"):
            c.sendall('good bye'.encode())
            c.close()
            print("client gone :)")
            break
        massage = input()
        c.sendall(massage.encode())
except KeyboardInterrupt:
    print("keyboard interrupt!")
    s.close()