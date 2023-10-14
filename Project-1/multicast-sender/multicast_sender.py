# This script serves as a multicast sender for our distributed system.
# It uses UDP (User Datagram Protocol) for multicast communication.
# The concept of multicast messaging is adapted from existing multicast protocols.
# Source Protocol: Multicast Messaging, Original Concepts
# Original Design: [Author Name]


import socket

def send_multicast_communication(port, message):
    # Creating a new socket
    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multicast_group = ('224.0.0.1', port)
    # Try sending a message
    try:
        multicast_socket.sendto(message.encode(), multicast_group)
        print(f"Sent multicast message: {message}")
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    send_multicast_communication(port, "max")
    

