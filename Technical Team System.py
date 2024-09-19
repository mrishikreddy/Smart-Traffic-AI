import socket
try:
    socket.create_connection(("8.8.8.8", 53), timeout=3)
except OSError:
    print("Could not connect to internet, check your wifi connection")
    exit(0)
    

s = socket.socket()
s.bind(("localhost",45320))
s.listen(3)
c,addr=s.accept()
print("technical team side")
p=c.recv(1024).decode()
print(p)
c.close()
s.close
exit()
