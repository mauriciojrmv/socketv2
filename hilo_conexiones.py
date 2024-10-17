import threading  # Importa threading para crear hilos
from hilo_comunicacion import HiloComunicacion  # Importa la clase HiloComunicacion

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
            cliente_ip = direccion[0]  # Obtener la IP del cliente

            # Verificar si la IP ya está conectada
            if cliente_ip in self.servidor.sesiones_activas:
                # Enviar un mensaje de rechazo antes de cerrar la conexión
                mensaje_rechazo = "Conexión rechazada: Ya existe una sesión activa desde esta IP."
                cliente_socket.send(mensaje_rechazo.encode())
                print(f"Conexión rechazada para el cliente {cliente_ip}.")
                cliente_socket.close()  # Rechazar la conexión
            else:
                print(f"Conexión aceptada desde {direccion}")
                # Agregar la nueva IP a la lista de sesiones activas
                self.servidor.sesiones_activas.add(cliente_ip)

                # Agregar la nueva conexión (socket) a la lista de conexiones
                self.servidor.get_conexiones().append(cliente_socket)
                print(f"Conexiones activas: {len(self.servidor.get_conexiones())}")
                
                # Crear un nuevo hilo para manejar la comunicación con este cliente
                hilo_comunicacion = HiloComunicacion(cliente_socket, self.servidor, direccion)
                hilo_comunicacion.start()  # Iniciar el hilo para gestionar los mensajes del cliente
