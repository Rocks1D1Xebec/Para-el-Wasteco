import socket

servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 5000))
servidor.listen(1)

print("Servidor esperando conexion.....")
conexion, direccion= servidor.accept()
print("Cliente conectado desde : ", direccion)

mensaje=conexion.recv(1024).decode()
print("Mensaje recivido: ", mensaje)

conexion.send("Mensaje recivido correctamente".encode())
conexion.close()
servidor.close()
# enfasis en lectura tecnica