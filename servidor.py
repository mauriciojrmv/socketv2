import socket
from hilo_conexiones import HiloConexiones

# Clase 2: Servidor - Configura el socket y maneja las conexiones
class Servidor:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        # Crear el socket TCP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conexiones = []

    def iniciar_servidor(self):
        # Vincular el socket a la dirección y puerto
        self.server_socket.bind((self.host, self.port))
        # Escuchar conexiones simultáneas
        self.server_socket.listen(20)
        print(f"Servidor escuchando en {self.host}:{self.port}")

        # Bucle infinito para aceptar nuevas conexiones
        while True:
            cliente_socket, direccion = self.server_socket.accept()
            print(f"Conexión aceptada desde {direccion}")
            # Crear un nuevo hilo para manejar la conexión
            hilo_conexion = HiloConexiones(cliente_socket, self, direccion)
            hilo_conexion.start()
