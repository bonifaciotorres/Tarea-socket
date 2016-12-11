import socket
import sys
from thread import *
from subprocess import call
import os

HOST = "" #Escuchara por todas las interfaces
PORT = 3333
var = ["arch"]

s = socket.socket(
		socket.AF_INET, socket.SOCK_STREAM)
print "Socket Creado"

n = 10
try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print "Error al crear Socket. Error code: " + str(msg[0]) + ",Mensaje de Error; " + msg[1]
	sys.exit()

print "Enlace Via Socket Activo"

s.listen(n) #Encolara in maximo de 5 conexiones
print "Socket escuchando en puerto " +str(PORT)
"""
#Espera y acepta las conexiones
conn, addr = s.accept()

#Muestra informacion del cliente
print "Conectado con " + addr[0] + ":" + str(addr[1])
"""

#Funcion 
def hilo_cliente(conn):
	#Enviar un mensaje al cliente cuando se conecte
	conn.send("Bienvenido al server. Escriba algo y presione INTRO")
	#Civlo infinito de es
	while True:
		#Espera y acepta las conexiones
		#conn, addr = s.accept()
		#print "Conectado con " +addr[0] + ":" + str(addr[1])
		
		data = conn.recv(1024)
		k="Bebida creada por los salvadorenos la cualcontiene extracto de maiz, el cual se le mezcla agua y se convierte en una especie de atol; el cual se acompana de un dulce de atado o batido de dulce"
		print data	
			
		if data =="Chilate":
			respuesta = k
				
		tree=raw_input('enviar al cliente: ')
		respuesta = tree
		
		
		
		if not data:
			break
					
		elif data == "q":
			respuesta= call(var)
			
		conn.sendall(respuesta)
	conn.close()
"""
while True:
	#Espera y acepta las conexiones
	conn, addr = s.accept()
	print "Conectado con " +addr[0] + ":" + str(addr[1])
	
	data = conn.recv(1024)
	respuesta = "OK..." + data
	print data
	if not data:
		break
	conn.sendall(respuesta)
conn.close()
s.close()
"""

#Comunicandose con el cliente
while 1:
	#Espera para aCEPTAR CONEXIONES
	conn, addr = s.accept()
	print "Conectado con " + addr[0] + ":" + str(addr[1])
	
	#Inicia un nuevo hilo el cual recine 2 parametros: el hilo y la conexion
	start_new_thread(hilo_cliente,(conn,))
s.close()
