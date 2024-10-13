import threading

# Clase 4: HiloComunicacion - Maneja la comunicación entre el servidor y el cliente
class HiloComunicacion(threading.Thread):
    def __init__(self, cliente_socket, servidor, direccion):
        super().__init__()
        self.cliente_socket = cliente_socket  # Socket del cliente conectado
        self.servidor = servidor  # Referencia al servidor para modificar la lista de conexiones
        self.direccion = direccion  # Dirección IP del cliente

    def run(self):
        conectado = True  # Variable de control para gestionar la conexión
        while conectado:
            try:
                # Recibe el mensaje del cliente
                mensaje = self.cliente_socket.recv(1024).decode()

                if mensaje:  # Si hay un mensaje
                    print(f"Mensaje recibido de {self.direccion}: {mensaje}")
                    # Envía una respuesta de vuelta al cliente
                    self.cliente_socket.send(f"Tu mensaje desde {self.direccion} es: {mensaje}".encode())
                else:  # Si no hay mensaje, significa que el cliente cerró la conexión
                    conectado = False

            except ConnectionResetError:
                # Si hay un error de conexión (por ejemplo, el cliente cierra abruptamente)
                print(f"Error de conexión con el cliente {self.direccion}.")
                conectado = False  # Cambia el estado de conexión para salir del bucle

        # Cerrar el socket cuando termine la comunicación
        self.cliente_socket.close()
        
        # Eliminar la conexión de la lista de conexiones activas
        self.servidor.get_conexiones().remove(self.cliente_socket)
        print(f"Cliente {self.direccion} se ha desconectado.")
        
        # Mostrar la cantidad de conexiones activas
        print(f"Conexiones activas: {len(self.servidor.conexiones)}")