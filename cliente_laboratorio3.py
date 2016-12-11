import socket
TCP_IP = "172.20.3.195"
TCP_PORT = 3333
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

while True:
	data = str(s.recv(BUFFER_SIZE))
	
	print "EL server dijo: ", data
	msg = raw_input("Ingrese un texto: ")
	if msg != 0:
		s.send(msg)
		
	else:
		break
		print "hasta luego"
		s.close()
