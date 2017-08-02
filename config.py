# Configuracion de lectorRFID generica
# estas variables se sobre escriben en el archivo config.local.py

MYSQL_SERVIDOR = "localhost"
MYSQL_BD = "raspberrypi"
MYSQL_USUARIO = "raspberrypi"
MYSQL_CONTRASENA = "contrasena_super_secreta"

# Carga la configuracion local desde el archivo config.local.py
try:
	from config_local import *
except Exception, e:
	print "ERROR: " + str(e)
