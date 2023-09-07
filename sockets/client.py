import socket
import os

# Configura el cliente
HOST = '142.44.243.204'  # Reemplaza esto con la dirección IP del servidor
PORT = 12345  # Puerto de comunicación del servidor

# Crea el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Conexión establecida con el servidor. Escribe comandos o 'exit' para salir.")

command_buffer = ""

while True:
    user_input = input("> ")

    if user_input.lower() == 'exit':
        break

    # Si se encuentra un punto y coma (;) en la entrada, envía el comando al servidor
    if ';' in user_input:
        command_buffer += user_input + "\n"  # Agrega el comando al búfer
        client_socket.send(command_buffer.encode())
        command_buffer = ""  # Limpia el búfer después de enviar los comandos
    else:
        command_buffer += user_input + "\n"  # Agrega el comando al búfer

    # Recibe y muestra la respuesta del servidor
    response = client_socket.recv(4096).decode()
    print(response)

    # Limpia la consola
    os.system('cls' if os.name == 'nt' else 'clear')

# Cierra la conexión
client_socket.close()
