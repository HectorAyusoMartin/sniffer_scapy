Pequeño Script usando Scapy, para la captura, manejo y filtrado de paquetes TCP - UDP - ICMP de distintos tipos de conexiones de red.
El Scrip cuenta con las funciones de:


    -start_capture()
    -read_capture()
    -filter_by_protocol()
    -filter_by_text()
    -print_packets_details()
    -export_to_pcap()


El proyecto también contiene los archivos .venv y requirements.txt. El archivo .venv corresponde con un entorno virtual, el cual se usa para el uso de instalación de dependencias
y librerias, como Scapy, de una forma mas localizada solamente en este proyecto.
Para instalar todas las dependencias necesarias para ejecutar el script, se deberá a traves de PIP, ejecutar el siguiente comando:

pip install -r requierements.txt

Este proyecto unicamente hace uso de la biblioteca de terceros "Scapy"

Scapy es básicamente el "cuchillo suizo" de las redes en Python. Con él puedes crear, enviar, analizar y manipular paquetes de red de manera súper flexible. 
Es como tener el superpoder de ver y modificar el tráfico de red a tu antojo, sin complicaciones ni rollos burocráticos. 
¡Puro poder digital en pocas líneas de código!






NOTAS:

1- En este Script hemos cogido agilidad aplicando listas por compresión en vez de .appends en bucles for.

2- La Libreria Scapy, mucho mas estable para hacer sniffing de paquetes de red que PyShark.

3- TODO: imposible controlar la excepcion KeyboardInterrupt. Timeout de 10 sec para finalizar la captura de paquetes
         Commit2: Solucionado. Estaba mal configurada la interfaz de red.

