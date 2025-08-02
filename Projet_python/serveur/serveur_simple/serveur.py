import socket
port = 4444
host = "0.0.0.0"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(1)
print("[+] En attente de connexion sur {}:{}".format(host, port))
client_socket, client_address = server.accept()
print("[+] Connexion établie avec {}".format(client_address))

while True:
    cmd = input(">>>")
    if cmd.lower() == "exit":
        client_socket.close()
        print("[+] Connexion fermée.")
        break
    if cmd:
        client_socket.send(cmd.encode())
        response = client_socket.recv(4096).decode()
        print(response)

    client_socket.send(cmd.encode())
    response = client_socket.recv(4096).decode()
    print(response)

client.close()
print("[+] Connexion fermée.")  
