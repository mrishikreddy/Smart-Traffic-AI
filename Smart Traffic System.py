import socket
import time
try:
    socket.create_connection(("8.8.8.8", 53), timeout=3)
except OSError:
    print("Could not connect to internet, check your wifi connection")
    exit(0)
    
c = socket.socket()
c.connect(("localhost",55321))
print("Smart System is on")
count = 0
while 1:
    if count==5:
        break
    count+=1
    c.send(bytes("System Status : Ok","utf-8"))
    time.sleep(3)
c.close()
