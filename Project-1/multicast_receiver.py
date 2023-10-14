# This script functions as a multicast receiver in our distributed system.
# It listens for multicast messages using the UDP protocol.
# The basic multicast principles and usage of UDP are based on existing multicast protocols.
# Source Protocol: Multicast Messaging, Original Concepts
# Original Design: [Author Name]


import socket
import threading
from communication_logging import log_communication

def receive_multicast_messages(host, port):
    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multicast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    multicast_socket.bind((host, port))
    multicast_group = '224.0.0.1'
    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_group) + socket.inet_aton(host))

    while True:
        message, client_address = multicast_socket.recvfrom(1024)
        source_ip, source_port = client_address
        log_communication(source_ip, host, source_port, port, "UDP", "Multicast", message)
        print(f"Received broadcast message from {source_ip}:{source_port}: {message.decode()}")
        

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5001
    broadcast_thread = threading.Thread(target=receive_multicast_messages, args=(host, port))
    broadcast_thread.start()