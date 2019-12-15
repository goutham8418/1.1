import socket
import time
start = 80
place=123123
while True:
    start=time.time()
    s=socket.socket()
    s.connect(("52.50.216.204",9999))
    d=s.recv(1024)
    print(str.encode(str(int(d[0:5])*int(d[6:11])/int(d[12:17]))))
    place=start - time.time()
    print (place)
    if (place<=0.098 and place>0):
        s.sendall(str.encode(str(int(d[0:5])*int(d[6:11])/int(d[12:17]))))
        print(s.recv(1024))

