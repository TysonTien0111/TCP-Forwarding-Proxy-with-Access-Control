import socket

HOST = "127.0.0.1"
SERVER_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, SERVER_PORT))
    server_socket.listen()
    proxy_speaking_connection, proxy_speaking_address = server_socket.accept()

    with proxy_speaking_connection:
        client_message = proxy_speaking_connection.recv(1024)
        client_message = eval(client_message.decode("utf-8")) # Converting String to Dictionary

        server_message = "pong"

        print(f"Server ('{HOST}', {SERVER_PORT}) has received a message from the Proxy Server {proxy_speaking_address}.")
        print(f"Server ('{HOST}', {SERVER_PORT}) has extracted the Proxy Server IP {proxy_speaking_address}.")
        print(f"Server ('{HOST}', {SERVER_PORT}) is replying to the Client ('{client_message.get("client_ip")}', {client_message.get("client_port")}) via the Proxy Server route {proxy_speaking_address} with the message \"{server_message}\".")

        proxy_speaking_connection.sendall(server_message.encode("utf-8"))