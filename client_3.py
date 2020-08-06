from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("127.0.0.1",1234))
except ConnectionRefusedError:
    print("can't connect to server!")

try:
    while True:
        message = input()
        while not message:
            message = input()
        s.sendall(message.encode())
        data = s.recv(10000).decode()
        print(data)
        if (data == "good bye"):
            s.sendall("good bye".encode())
            s.close()
            break

except KeyboardInterrupt:
    print("keyboard interrupt!")
    s.close()