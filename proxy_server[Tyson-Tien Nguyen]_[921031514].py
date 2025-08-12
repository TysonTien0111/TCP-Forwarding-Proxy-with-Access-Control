import json
import socket

HOST = "127.0.0.1"
PROXY_LISTENING_PORT = 65431
PROXY_SPEAKING_PORT = 65430

banned_addresses = {
    "server_ip": ("175.64.233.247", "104.250.193.145", "175.82.49.219"),
    "server_port": (34392, 58275, 10200),
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_listening_socket:
    proxy_listening_socket.bind((HOST, PROXY_LISTENING_PORT))
    proxy_listening_socket.listen()
    client_connection, client_address = proxy_listening_socket.accept()

    with client_connection:
        server_information = client_connection.recv(1024)
        server_information = eval(server_information.decode("utf-8")) # Converting String to Dictionary
        server_ip = server_information.get("server_ip")
        server_port = server_information.get("server_port")
        client_message = server_information.get("message")

        print(f"Proxy Server ('{HOST}', {PROXY_LISTENING_PORT}) has received a message from the Client {client_address}.")
        print(f"Proxy Server ('{HOST}', {PROXY_LISTENING_PORT}) has extracted the Server's IP ('{server_ip}', {server_port}) from the Client's {client_address} message.")
        
        if ((server_ip not in banned_addresses.get("server_ip")) and (server_port not in banned_addresses.get("server_port"))):
            print(f"Proxy Server ('{HOST}', {PROXY_LISTENING_PORT}) has checked that the Server's IP ('{server_ip}', {server_port}) is not a banned address, proceeding with forwarding Client's {client_address} message to the Server ('{server_ip}', {server_port}).")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_speaking_socket:
                proxy_speaking_socket.bind((HOST, PROXY_SPEAKING_PORT))

                data = {
                    "client_ip": client_address[0],
                    "client_port": client_address[1],
                    "message": client_message
                }
                            
                proxy_speaking_socket.connect((server_ip, server_port))
                proxy_speaking_socket.sendall(json.dumps(data).encode("utf-8"))

                print(f"Proxy Server ('{HOST}', {PROXY_SPEAKING_PORT}) is now sending the message \"{client_message}\" on behalf of the Client {client_address} to the Server ('{server_ip}', {server_port}).")
                server_reply = proxy_speaking_socket.recv(1024)
                print(f"Proxy Server ('{HOST}', {PROXY_SPEAKING_PORT}) has received the Server's ('{server_ip}', {server_port}) message reply to the Client {client_address}.")
                print(f"Proxy Server ('{HOST}', {PROXY_SPEAKING_PORT}) is now forwarding the Server's ('{server_ip}', {server_port}) message to the Client {client_address}.")

                client_connection.sendall(server_reply)
        else:
            print(f"Proxy Server ('{HOST}', {PROXY_LISTENING_PORT}) has detected that the Server's IP ('{server_ip}', {server_port}) is a banned address. Proxy Server shall not proceed further and reply to the Client {client_address} with an \"Error\" response.")

            client_connection.sendall(b"Error") 