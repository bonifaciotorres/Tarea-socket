#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket # for sockets
import sys
import os
import shlex
import subprocess
from thread import * #agregamos paquete para la programacion por hilos
from subprocess import call
from subprocess import PIPE, Popen


HOST = '' #Escuchara por todas las interfaces 
PORT = 3333 # Usamos un puerto de numeracion alta para no interferir





f = ["ls","-lSr","|more"]





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket Creado"

try:
	s.bind((HOST, PORT))
except socket.error, msg:
	print "Error al crear Socket. Error code: " + str (msg[0]) + "Mensaje de Error: " + msg[1]
	sys.exit()
	
print "Enlace via Socket Activo"

s.listen(10) #Encolara un maximo de 10 conexiones
print "Socket escuchando en puerto " + str(PORT)

def hilo_cliente(conn):
	#enviar un mensaje al cliente cuando se conecte
	conn.send("Bienvenido al servidor. Escriba algo y presione ENTER ")
	
	while True:
		#conn, addr = s.accept()
		#Muestra informacion del cliente
		#print "Conectado con " + addr[0] + ';' + str(addr[1])
	
		data = conn.recv(1024)
		respuesta="No Puedo procesar su termino, intente con otra función o termine la comunicación"
		print data		
		if not data:
			break
		elif data == 'Chilate':
			respuesta = "Bebida creada por los salvadorenos la cual contiene extracto de maiz, el cual se le mezcla agua y se convierte en una especie de atol; el cual se acompana de un dulce de atado o batido de dulce"
			
		elif data == 'Python':
			respuesta = "Es un lenguaje de programación interpretado cuya filosofia hace hincapie en una sintaxis que favorezca un codigo legible"
		
		elif data == 'Cthulhu':
			respuesta = "es un personaje extraido de la literatura de H.P. Lovecraft, Lovecraft formo en algunos de sus relatos, una mitologia del horror basada en la existencia de universos paralelos y seres provenientes de ellos"
			
		elif data == 'Megadeth':
			respuesta = "Banda de metal"
		
		elif data == 'Pokemon':
			respuesta = "Juego de consola"
			
		elif data == 'Nintendo':
			respuesta = "Compañia de video juegos"	
		
		elif data == 'Linux':
			respuesta = "sistema operativo libre"
			
		elif data == 'Windows':
			respuesta = "sistema operativo privado"
			
		elif data == 'Hola que hace':
			respuesta = "tratando de hablar con un humano"		
			
		elif data == 'XD':
			respuesta = "se utiliza en vez de jajajajajajajajajaja"
		
		
		elif data == "arquitectura de la pc":	
			proceso = Popen(["arch"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "kernel":	
			proceso = Popen(["uname","-r"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "fecha del sistema":	
			proceso = Popen(["date"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "almanaque de 2011":	
			proceso = Popen(["cal","2011"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "particiones":	
			proceso = Popen(["df","-h"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "uso de memoria":	
			proceso = Popen(["cat","/proc/meminfo"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "PCI":	
			proceso = Popen(["lspci","-tv"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "USB":
				
			#respuesta = str(subprocess.call(shlex.split(h)))
			
			
			#respuesta=call(h)
			proceso = Popen(["lsusb","-tv"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "almanaque julio":
				
			proceso = Popen(["cal","07","2011"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
		
		elif data == "ficheros de directorio":	
			proceso = Popen(["ls","-F"], stdout=PIPE, stderr=PIPE)
			error_econtrado = proceso.stderr.read()
			proceso.stderr.close()
			listado = proceso.stdout.read()
			proceso.stdout.close()
			respuesta =str(proceso)
			respuesta =str(listado)
			
			
		conn.sendall(respuesta)
		
		
	#cerrar conexion
	conn.close()

while 1:
	#espera para aceptar conexiones
	conn, addr = s.accept()
	print "conectado con " + addr[0] + ';' + str (addr[1])
	
	#inicia un nuevo hilo el cual recibe 2 parametros el hilo
	
	start_new_thread(hilo_cliente, (conn,))
s.close()
