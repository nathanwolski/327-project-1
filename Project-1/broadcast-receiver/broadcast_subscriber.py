# This code acts as a broadcast subscriber in our distributed system.
# It uses RabbitMQ as a message broker to receive broadcast messages.
# The Publish-Subscribe pattern and message exchange are based on existing broadcast protocols.
# Source Protocol: Broadcast Pattern, Original Concepts
# Original Design: Nathanael Wolski


import socket
import communication_logging as cl

def listen_for_broadcast():
    # Define the IP address and port to listen on
    ip_address = "0.0.0.0"  # Listen on all available interfaces
    port = 12345  # Use a port of your choice

    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP address and port
    udp_socket.bind((ip_address, port))

    print(f"Listening for broadcast messages on {ip_address}:{port}...")
    # Log message data while script listens for messages
    while True:
        message, client_address = udp_socket.recvfrom(1024)
        source_ip, source_port = client_address
        cl.log_communication(source_ip, ip_address, source_port, port, "UDP", "Broadcast", message)
        print(f"Received broadcast message from {source_ip}:{source_port}: {message.decode()}")
        
def main():
    listen_for_broadcast()

if __name__ == "__main__":
    main()
