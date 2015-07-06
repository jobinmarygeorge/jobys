import socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 9998
host = socket.gethostname()
serversocket.bind((host,port))
serversocket.listen(5)
while True:
	clientsocket,addr = serversocket.accept()
print("got connection");
p = 'hai iam jobin'
clientsocket.send(p)
clientsocket.close()

