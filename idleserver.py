import socket
import time

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print host , port
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
i=0
while True:

    try:
        data = conn.recv(1024)

        if not data: break

        print "Client Says: "+data
        conn.sendall("Server Says:hi")
        if i==0:
            time.sleep(1);

        i+=1
        
        if i%5 == 0:
            time.sleep(5);



    except socket.error:
        print "Error Occured."
        break

conn.close()

