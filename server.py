#server.py  
import socket  
import json
def getipaddrs(hostname):#只是为了显示IP，仅仅测试一下  
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)  
    return [x[4][0] for x in result]  
  
host = '0.0.0.0'#为空代表为本地host  
hostname = socket.gethostname()  
hostip = getipaddrs(hostname)  
print('host ip', hostip)#应该显示为：127.0.1.1  
port = 12345     # Arbitrary non-privileged port  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.bind((host, port))  
s.listen(4) 
conn, addr = s.accept()  
print('Connected by', addr) 
while True:  
    raw_data = conn.recv(10240)  
    if not raw_data: break  

    #conn.sendall(data)#把接收到数据原封不动的发送回去  
    #print('Received', repr(raw_data))

    if  b'text' in raw_data and b'from' in raw_data:

        data = raw_data[0:raw_data.find(b'}', 1) + 1]
        a=data[data.index(b'{'):].decode("utf8")
        #print(a)
        text = json.loads(a)["text"]
        if 'B' in text:
            print('按键模式:'+text[1])
            received = '按键模式:'+text[1]
        elif 'J' in text:
            print('摇杆模式:'+text[1])
            received = '摇杆模式:'+text[1]
        elif 'G' in text:
            print('重力模式:'+text[1])
            received = '重力模式:'+text[1]
        elif 'F' in text:
            print('路径模式:'+text[1])
            received = '路径模式:'+text[1]
        else:
            print('语音模式:'+ text)
            received = '语音模式:'+text[1]
        with open('received.txt','w') as f:
            f.write(received)

conn.close()