import socket

cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1",5000))

cliente.send("Hola servidor, soy un Cliente".encode())
respuesta=cliente.recv(1024).decode()
print("Respuesta del servidor", respuesta)

cliente.close()