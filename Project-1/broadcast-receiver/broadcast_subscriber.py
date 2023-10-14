# This code acts as a broadcast subscriber in our distributed system.
# It uses RabbitMQ as a message broker to receive broadcast messages.
# The Publish-Subscribe pattern and message exchange are based on existing broadcast protocols.
# Source Protocol: Broadcast Pattern, Original Concepts
# Original Design: Nathanael Wolski


import socket
import threading
import communication_logging as cl

def receive_broadcast_messages(host, port):
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    broadcast_socket.bind((host, port))

    while True:
        message, client_address = broadcast_socket.recvfrom(1024)
        source_ip, source_port = client_address
        cl.log_communication(source_ip, host, source_port, port, "UDP", "Broadcast", message)
        print(f"Received broadcast message from {source_ip}:{source_port}: {message.decode()}")
        
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 80
    broadcast_thread = threading.Thread(target=receive_broadcast_messages, args=(host, port))
    broadcast_thread.start()

