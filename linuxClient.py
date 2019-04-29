import socket   
s = socket.socket()         
host = socket.gethostname() 
port = 12306 
s.connect((host, port))                           
while(1):
    raw_data = s.recv(10240)  
    if not raw_data: break
    if len(raw_data) != 0:
        print(raw_data.decode())
s.close() 