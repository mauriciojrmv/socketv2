import configparser
from servidor import Servidor

# Clase 1: Main - Ejecuta las clases de conexión y administración de hilos
class Main:
    def __init__(self):
        # Crear una instancia del lector de configuraciones
        config = configparser.ConfigParser()
        # Leer el archivo config.ini
        config.read('config.ini')

        # Asignar el host y el puerto desde el archivo de configuración
        self.host = config['servidor']['host']
        self.port = int(config['servidor']['port'])

        # Crear una instancia del servidor con el host y puerto obtenidos del archivo
        self.servidor = Servidor(self.host, self.port)

    def run(self):
        # Ejecutar el servidor
        self.servidor.iniciar_servidor()


# Iniciar la aplicación
if __name__ == "__main__":
    main = Main()  # Instancia la clase Main
    main.run()  # Ejecuta el método run, que inicia el servidor