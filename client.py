import json
import socket

HOST = "127.0.0.1"
SERVER_PORT = 65432
PROXY_LISTENING_PORT = 65431

print("Please enter a 4-letter string.")
input_message = input()

data = {
    "server_ip": HOST,
    "server_port": SERVER_PORT,
    "message": input_message
}

str_data = json.dumps(data) # Converting Dictionary to String.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PROXY_LISTENING_PORT))
    client_socket.sendall(str_data.encode("utf-8"))

    print(f"Client ('{HOST}', {client_socket.getsockname()[1]}) is sending {str_data} to the Server ('{HOST}', {SERVER_PORT}) via the Proxy Server route ('{HOST}', {PROXY_LISTENING_PORT}).")

    proxy_reply = client_socket.recv(1024)

    if (proxy_reply.decode("utf-8") == "Error"):
        print(f"Client ('{HOST}', {client_socket.getsockname()[1]}) has received an \"Error\" response from the Proxy Server ('{HOST}', {PROXY_LISTENING_PORT}). The Proxy Server ('{HOST}', {PROXY_LISTENING_PORT}) has stated that the Server's IP ('{data.get("server_ip")}', {data.get("server_port")}) is banned and shall not proceed further.")
    else:
        print(f"Client ('{HOST}', {client_socket.getsockname()[1]}) received response from the Server ('{HOST}', {SERVER_PORT}). Server ('{HOST}', {SERVER_PORT}) responded to the Client ('{HOST}', {client_socket.getsockname()[1]}) with \"{proxy_reply.decode("utf-8")}\" via the Proxy Server route ('{HOST}', {PROXY_LISTENING_PORT}).")