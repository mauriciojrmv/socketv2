from servidor import Servidor

# Clase 1: Main - Ejecuta las clases de conexión y administración de hilos
class Main:
    def __init__(self):
        # Solicitar al usuario el host y puerto de manera dinámica
        self.host = input("Introduce la dirección IP o 'localhost' para escuchar: ") or 'localhost'
        self.port = int(input("Introduce el puerto (por defecto 8080): ") or 8080)

        # Crear una instancia del servidor con el host y puerto dinámico
        self.servidor = Servidor(self.host, self.port)

    def run(self):
        # Ejecutar el servidor
        self.servidor.iniciar_servidor()


# Iniciar la aplicación
if __name__ == "__main__":
    main = Main()  # Instancia la clase Main
    main.run()  # Ejecuta el método run, que inicia el servidor
