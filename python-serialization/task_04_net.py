#!/usr/bin/env python3
import socket
import json


def start_server(host="127.0.0.1", port=65432):
    """Start a simple TCP server that receives JSON data and prints a dict."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)

        conn, _ = server_socket.accept()
        with conn:
            chunks = []
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                chunks.append(data)

            raw = b"".join(chunks).decode("utf-8")
            received_dict = json.loads(raw)

            print("Received Dictionary from Client:")
            print(received_dict)

    except (OSError, json.JSONDecodeError):
        return None
    finally:
        server_socket.close()


def send_data(data_dict, host="127.0.0.1", port=65432):
    """Connect to the server, serialize dict as JSON, and send it."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        payload = json.dumps(data_dict).encode("utf-8")
        client_socket.sendall(payload)
    except (OSError, TypeError):
        return None
    finally:
        client_socket.close()
