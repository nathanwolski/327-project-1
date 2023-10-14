# This script functions as a multicast receiver in our distributed system.
# It listens for multicast messages using the UDP protocol.
# The basic multicast principles and usage of UDP are based on existing multicast protocols.
# Source Protocol: Multicast Messaging, Original Concepts
# Original Design: [Author Name]


import socket
import communication_logging as cl

def listen_for_multicast():
    # Multicast group and port
    MULTICAST_GROUP = '224.0.0.1'
    MULTICAST_PORT = 5000

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the multicast address and port
    sock.bind(('', MULTICAST_PORT))

    # Tell the kernel to join the multicast group
    mreq = socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0')
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    # Log messages while the script is listening
    while True:
        message, client_address = sock.recvfrom(1024)
        source_ip, source_port = client_address
        cl.log_communication(source_ip, MULTICAST_GROUP, source_port, MULTICAST_PORT, "UDP", "Multicast", message)
        print(f"Received multicast message from {source_ip}:{source_port}: {message.decode()}")

def main():
    listen_for_multicast()
    

if __name__ == "__main__":
    main()