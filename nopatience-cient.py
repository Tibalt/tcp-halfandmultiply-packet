import socket
import time

host = 'localhost'
port = 12345                   # The same port as used by the server

data = '1'*100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
i=0
while(1):
        try: 
            s.send(b'd'+str(i)+data+'d')
            print(i)
            i+=1
        except socket.error as e : 
            print(e) 
            break;
#data = s.recv(1024)
s.close()
#print('Received', repr(data))

