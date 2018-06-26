# RaspberryPi-RFID
Ejemplo de un lector de tarjetas RFID que activa un relay usando una Raspberry Pi.

## Depdendencias ##
Las siguientes dependencias son necesarias para que el programa funcione correctamente:

* Librería SPI-Py https://github.com/lthiery/SPI-Py

  Clonar o descargar el repositorio, cambiarse al directorio donde esta la librería e instalar con 

  sudo python setup.py install

* Librería MFRC522-python https://github.com/mxgxw/MFRC522-python

  Clonar o descargar el repositorio y luego copiar la librería MFRC522.py en la carpeta de nuestro proyecto.

## Instalación ##
El programa lee desde una base de datos el identificador de la tarjeta RFID, por lo cual se debe instalar previamente el motor de base de datos MySQL.

Luego se debe crear la base de datos raspberrypi y cargar la tabla tarjeta a partir del script sql que esta dentro de la carpeta sql en este repositorio.

## Configuración ##

Para configurar el programa se debe crear el archivo config_local.py, cuyo contenido debe ser

```
MYSQL_SERVIDOR = "localhost"
MYSQL_BD = "raspberrypi"
MYSQL_USUARIO = "raspberrypi"
MYSQL_CONTRASENA = "contrasena_super_secreta"
```

Este archivo sobre escribe la configuración y se debe reemplazar por los valores que usas en tu proyecto, al estar este archivo dentro del gitignore, es ignorado por git y no es sincronizado con el directorio, protegiendo asi tus configuraciones y en especial tu contraseña.

## Ejecutar ##
Para ejecutar el programa python lectorRFID.py se debe usar sudo ya que se necesitan privilegios de super usario para acceder a los puertos GPIO.

sudo python lectorRFID.py

## Contribuciones ##
Siéntase libre de clonar este repositorio y enviar sus contribuciones mediante pull request.

## Contacto ##
Cualquier duda o sugerencia puedes escribirnos a contacto@iot.cl

