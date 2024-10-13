import threading
from hilo_comunicacion import HiloComunicacion

# Clase 3: HiloConexiones - Administra las conexiones de los clientes en hilos separados
class HiloConexiones(threading.Thread):
    def __init__(self, server_socket, servidor):
        super().__init__()
        self.server_socket = server_socket  # Socket del servidor
        self.servidor = servidor  # Referencia al servidor que maneja las conexiones

    def run(self):
        # Bucle infinito para aceptar nuevas conexiones
        while True:
            cliente_socket, direccion = self.server_socket.accept()  # Espera una conexión entrante
            print(f"Conexión aceptada desde {direccion}")
            # Agregar la nueva conexión a la lista de conexiones
            self.servidor.get_conexiones().append(cliente_socket)
            print(f"Conexiones activas: {len(self.servidor.conexiones)}")
            
            # Crear un nuevo hilo para manejar la comunicación con este cliente
            hilo_comunicacion = HiloComunicacion(cliente_socket, self.servidor, direccion)
            hilo_comunicacion.start()  # Iniciar el hilo para gestionar los mensajes del cliente
