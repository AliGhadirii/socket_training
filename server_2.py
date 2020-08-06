from socket import *

dict = {}

s=socket(AF_INET, SOCK_DGRAM)
s.bind(("127.0.0.1",1234))

while True:
    data, addr = s.recvfrom(1024)
    print(addr,"is connected!")
    temp = data.decode()
    if (temp == "GET"):
        for i,j in dict.items():
            tosend = str(i)+':'
            for k in j:
                tosend += k + '/'
            s.sendto(tosend.encode(),i)
    if (temp[:temp.find(' ')] == "POST"):
        massage = temp[temp.find(' ') + 1:]
        if addr in dict.keys():
            dict[addr].append(massage)
        else:
            dict[addr]=[massage]


