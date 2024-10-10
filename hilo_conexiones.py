import threading
from hilo_comunicacion import HiloComunicacion

# Clase 3: HiloConexiones - Administra las conexiones de los clientes en hilos separados
class HiloConexiones(threading.Thread):
    def __init__(self, cliente_socket, servidor, direccion):
        super().__init__()
        self.cliente_socket = cliente_socket
        self.servidor = servidor
        self.direccion = direccion

    def run(self):
        # Agregar la nueva conexión a la lista de conexiones
        self.servidor.conexiones.append(self.cliente_socket)
        print(f"Conexiones activas: {len(self.servidor.conexiones)}")
        
        # Crear un nuevo hilo para manejar la comunicación con este cliente
        hilo_comunicacion = HiloComunicacion(self.cliente_socket, self.servidor, self.direccion)
        hilo_comunicacion.start()
