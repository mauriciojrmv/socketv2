# Proyecto de Sistemas Distribuidos - Servidor TCP Multihilo en Python

Este proyecto es parte de la materia Sistemas Distribuidos y tiene como objetivo implementar un servidor TCP multihilo utilizando sockets en Python. El servidor permite la conexión simultánea de varios clientes y gestiona la comunicación entre ellos y el servidor a través de hilos, asegurando una correcta distribución de la carga de trabajo.

## Descripción del Proyecto
El servidor TCP desarrollado puede aceptar múltiples conexiones de clientes y para cada conexión, crea un hilo independiente que gestiona tanto la conexión como la comunicación y las sesiones para evitar duplicidad. Cada cliente puede enviar mensajes al servidor, y este responde con un mensaje de eco. El proyecto aun no funciona como broadcast, en esta version se añadieron las sesiones para un mejor control de conexiones

## Estructura del Proyecto
El proyecto está organizado de manera modular, con cada funcionalidad importante en su propio archivo:


├── **main.py**               Archivo principal que ejecuta el servidor

├── **servidor.py**           Clase Servidor, gestiona las conexiones TCP

├── **hilo_conexiones.py**     Clase HiloConexiones, gestiona los hilos de conexiones

└── **hilo_comunicacion.py**   Clase HiloComunicacion, gestiona la comunicación cliente-servidor

└── **cliente.py**              Archivo principal que ejecuta el cliente

## Requisitos

**Python 3.x** (de preferencia la última versión estable)

## Ejecución

Ejecuta el archivo **main.py** para iniciar el servidor TCP

**python main.py**

El servidor estará escuchando en localhost en el puerto 8080.

## Conectar un cliente

Puedes conectar múltiples clientes para interactuar con el servidor en distintas ejecuciones de **cliente.py**