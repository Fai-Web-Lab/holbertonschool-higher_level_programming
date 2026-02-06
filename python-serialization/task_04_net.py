#!/usr/bin/python3
"""
Module for simple client-server network communication using JSON serialization.
"""
import socket
import json


def start_server():
    """
    Sets up a server that listens for a connection, receives serialized
    JSON data, and prints the deserialized dictionary.
    """
    host = 'localhost'
    port = 65432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Server listening on {host}:{port}...")

            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    received_dict = json.loads(data.decode('utf-8'))
                    print(f"Received Dictionary: {received_dict}")

    except Exception as e:
        print(f"Server error: {e}")


def send_data(dictionary):
    """
    Acts as a client that connects to the server and sends a
    serialized Python dictionary.

    Args:
        dictionary (dict): The dictionary to send to the server.
    """
    host = 'localhost'
    port = 65432

    if not isinstance(dictionary, dict):
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            serialized_data = json.dumps(dictionary).encode('utf-8')
            s.sendall(serialized_data)
            print("Data sent to server.")

    except ConnectionRefusedError:
        print("Error: Connection refused. Is the server running?")
    except Exception as e:
        print(f"Client error: {e}")
