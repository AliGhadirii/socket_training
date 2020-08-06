from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.sendto("POST salam payam 1".encode(), ("127.0.0.1", 1234))
s.sendto("POST salam payam 2".encode(), ("127.0.0.1", 1234))
s.sendto("POST salam payam 3".encode(), ("127.0.0.1", 1234))
s.sendto("POST salam payam 4".encode(), ("127.0.0.1", 1234))
s.sendto("GET".encode(), ("127.0.0.1", 1234))
data, addr = s.recvfrom(1024)
print(data.decode())