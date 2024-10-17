import socket

# Configuración del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))  # Conectar al servidor en localhost:8080

try:
    # Intentar recibir un posible mensaje de rechazo al inicio
    client_socket.settimeout(2)  # Establecer un tiempo de espera breve para la recepción
    try:
        mensaje_inicial = client_socket.recv(1024).decode()
        if "rechazada" in mensaje_inicial.lower():
            print(f"Servidor: {mensaje_inicial}")
            client_socket.close()  # Cerrar la conexión si fue rechazada
            exit()  # Salir del programa
    except socket.timeout:
        # Si no hay mensaje en 2 segundos, significa que la conexión fue aceptada
        print("Conexión aceptada. Puedes enviar mensajes.")

    # Continuar con el ciclo de envío de mensajes
    while True:
        # Envía un mensaje al servidor
        message = input("Escribe un mensaje: ")
        if not message:
            continue  # Si el mensaje está vacío, vuelve a pedir input

        client_socket.send(message.encode())

        # Recibe la respuesta del servidor
        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")

        if message.lower() == 'salir':
            break

except ConnectionAbortedError:
    print("Error: El servidor ha cerrado la conexión de forma abrupta.")
except ConnectionRefusedError:
    print("Error: No se pudo conectar al servidor.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    client_socket.close()
    print("Conexión cerrada.")
