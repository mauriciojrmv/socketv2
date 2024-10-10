import threading

# Clase 4: HiloComunicacion - Maneja la comunicación entre el servidor y el cliente
class HiloComunicacion(threading.Thread):
    def __init__(self, cliente_socket, servidor, direccion):
        super().__init__()
        self.cliente_socket = cliente_socket
        self.servidor = servidor
        self.direccion = direccion

    def run(self):
        while True:
            try:
                # Recibe el mensaje del cliente
                mensaje = self.cliente_socket.recv(1024).decode()
                if mensaje:
                    print(f"Mensaje recibido de {self.direccion}: {mensaje}")
                    # Envía una respuesta de vuelta al cliente
                    self.cliente_socket.send(f"Tu mensaje desde {self.direccion} es: {mensaje}".encode())
                else:
                    # Si no hay mensaje, el cliente ha cerrado la conexión
                    break
            except ConnectionResetError:
                # Si hay un error de conexión, cerrar el socket
                break

        # Cerrar el socket cuando termine la comunicación
        self.cliente_socket.close()
        
        # Eliminar la conexión de la lista de conexiones activas
        self.servidor.conexiones.remove(self.cliente_socket)
        print(f"Cliente {self.direccion} se ha desconectado.")
        
        # Mostrar la cantidad de conexiones activas
        print(f"Conexiones activas: {len(self.servidor.conexiones)}")
