import socket
try:
    socket.create_connection(("8.8.8.8", 53), timeout=3)
except OSError:
    print("Could not connect to internet, check your wifi connection")
    exit(0)
    

s = socket.socket()
tt = socket.socket()
s.bind(("localhost",55321))
tt.connect(("localhost",45320))
s.listen(3)
c,addr=s.accept()
print("server side")
print("connected with:",addr)
count = 0
while 1:
    p=c.recv(1024).decode()
    print(p)
    if p=="":
        print("switching to manual mode")
        c.close()
        s.close()
        tt.send(bytes("smart traffic system error","utf-8"))
        tt.close()
        break
c.close()
s.close()
exit()
