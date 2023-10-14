# This code implements a broadcast publisher for our distributed system.
# It is inspired by the Publish-Subscribe pattern and uses RabbitMQ as a message broker.
# The concept and messaging mechanisms are adapted from existing broadcast protocols.
# Source Protocol: Broadcast Pattern, Original Concepts
# Original Design: Nathanael Wolski


import socket

def publish_broadcast_message(port, message):
    # Create a new socket
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_address = ('0.0.0.0', port)
    # Try sending a message
    try:
        broadcast_socket.sendto(message.encode(), broadcast_address)
        print(f"Sent broadcast message: {message}")
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 80
    publish_broadcast_message(port, "billy")

