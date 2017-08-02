#!/usr/bin/python

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Raspberry Pi - Ejemplo de un lector de tarjetas RFID que activa un relay
# Lenguaje     : Python
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria SPI-Py https://github.com/lthiery/SPI-Py
#				 Libreria MFRC522-python https://github.com/mxgxw/MFRC522-python
# Web          : http://internetdelascosas.cl/

# Importa las librerias necesarias para el lector RFID
import RPi.GPIO as GPIO
import MFRC522
import signal
import time


from config import *

# Configura el relay
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Importa la libreria MySQL
import MySQLdb

# Variable global para controlar el ciclo principal
continuar = True

# Funcion y ciclo principal
def main():
	# Enlaza SIGINT (teclas Ctrl+C) con la funcion end_read()
	signal.signal(signal.SIGINT, finalizar)

	# Crea instancia de la clase MFRC522 para leer las tarjetas RFID
	MIFAREReader = MFRC522.MFRC522()

	print "--- lectorRFID - Programa demo de lectura de tarjetas RFID ---"
	print "    Presione Ctrl-C para detener ejecucion."

	while continuar:
		# Scanea tarjetas cercanas al lector
		(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

		# Si encuentra una tarjeta
		if status == MIFAREReader.MI_OK:
			print "Tarjeta detectada"
		
		# Obtiene el UID de la tarjeta
		(status,uid) = MIFAREReader.MFRC522_Anticoll()
		
		# Si hay un UID lo busca en la base de datos
		if status == MIFAREReader.MI_OK:

			card_id = str(uid[0]) + "." + str(uid[1]) + "." + str(uid[2]) + "." + str(uid[3])
			print "UID: " + card_id

			# Se conecta a la base de datos local
			db = MySQLdb.connect(host=MYSQL_SERVIDOR,
								user=MYSQL_USUARIO,
								passwd=MYSQL_CONTRASENA,
								db=MYSQL_BD)

			# Crea un cursos usando la conexion
			cursor = db.cursor()

			sql = "SELECT * FROM lectorRFID WHERE uid='" + card_id + "'"

			# Ejecuta el sql
			cursor.execute(sql)

			# Filas obtenidas como respuesta a la consulta
			filas = cursor.rowcount

			# Si obtiene filas, entonces la tarjeta esta en la base de datos
			if filas > 0:
				for registro in cursor:
					nombre = registro[1]
				print "Acceso permitido a " + str(nombre) + "."
				relay(RELAY_PIN)
			else:
				print "Acceso denegado."

			# Cierra cursor y conexion a base de datos
			cursor.close
			db.close

# Funcion que activa el relay
def relay(pin):
	# Activa relay
	GPIO.output(pin,1)
	print "Relay activado."
	time.sleep(2)

	# Desactiva relay
	GPIO.output(pin,0)
	print "Relay desactivado."

# Captura Ctrl+C y termina el ciclo infinito para terminar el programa
def finalizar(signal,frame):
    global continuar

    print "Ctrl+C presionado, programa finalizado."
    continuar = False
    GPIO.cleanup()


if __name__ == "__main__":
	main()