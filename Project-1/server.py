# # import socket
# # import threading
# # from broadcast_publisher import publish_message
# # from broadcast_subscriber import subscribe_messages
# # from multicast_sender import send_multicast_message
# # from multicast_receiver import receive_multicast_messages
# # from communication_logging import log_communication

# # # Define server parameters
# # host = 'localhost'
# # port = 8080

# # # Create a socket for the server
# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # # Bind the server to the specified host and port
# # server_socket.bind((host, port))

# # # Listen for incoming connections
# # server_socket.listen(5)
# # print(f"Server listening on {host}:{port}")

# # # Broadcast setup
# # broadcast_message = "This is a broadcast message."
# # broadcast_thread = threading.Thread(target=publish_message, args=(broadcast_message,))
# # broadcast_thread.start()

# # # Multicast setup
# # multicast_message = "This is a multicast message."
# # multicast_thread = threading.Thread(target=send_multicast_message, args=(multicast_message,))
# # multicast_thread.start()

# # # Subscribe to broadcast messages
# # subscribe_thread = threading.Thread(target=subscribe_messages)
# # subscribe_thread.start()

# # # Receive multicast messages
# # multicast_receiver_thread = threading.Thread(target=receive_multicast_messages)
# # multicast_receiver_thread.start()

# # while True:
# #     # Accept incoming connections
# #     client_socket, client_address = server_socket.accept()
# #     print(f"Accepted connection from {client_address}")

# #     # Implement your communication protocol logic here
# #     data = client_socket.recv(1024)

# #     # Process and respond to the data
# #     response = "Server: Received your message - " + data.decode()
# #     client_socket.send(response.encode())

# #     # Log the communication details
# #     log_communication(client_address[0], host, client_address[1], port, "TCP", len(data), "0x00")

# #     client_socket.close()

# import socket
# import threading
# from communication_logging import log_communication

# def receive_broadcast_messages(host, port):
#     broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     broadcast_socket.bind((host, port))

#     while True:
#         message, client_address = broadcast_socket.recvfrom(1024)
#         source_ip, source_port = client_address
#         log_communication(source_ip, host, source_port, port, "UDP", message, "Broadcast", len(message), "N/A")
#         print(f"Received broadcast message from {source_ip}:{source_port}: {message.decode()}")

# def receive_multicast_messages(host, port):
#     multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     multicast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     multicast_socket.bind((host, port))
#     multicast_group = '224.0.0.1'
#     multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_group) + socket.inet_aton(host))

#     while True:
#         message, client_address = multicast_socket.recvfrom(1024)
#         source_ip, source_port = client_address
#         log_communication(source_ip, host, source_port, port, "UDP", message, "Multicast", len(message), "N/A")
#         print(f"Received multicast message from {source_ip}:{source_port}: {message.decode()}")

# if __name__ == "__main__":
#     host = '0.0.0.0'
#     broadcast_port = 5000  # Use the appropriate broadcast port
#     multicast_port = 5001  # Use the appropriate multicast port

#     # Create separate threads for receiving broadcast and multicast messages
#     broadcast_thread = threading.Thread(target=receive_broadcast_messages, args=(host, broadcast_port))
#     multicast_thread = threading.Thread(target=receive_multicast_messages, args=(host, multicast_port))

#     broadcast_thread.start()
#     multicast_thread.start()
