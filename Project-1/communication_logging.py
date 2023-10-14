
import logging

# Configure the logger
logging.basicConfig(filename='communication.log', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def log_communication(
    source_ip, destination_ip, source_port, destination_port, protocol, communication_type, length_bytes
):
    log_entry = (
        f"[{communication_type}] "
        f"Source IP: {source_ip}, Destination IP: {destination_ip}, "
        f"Source Port: {source_port}, Destination Port: {destination_port}, "
        f"Protocol: {protocol}, Length (Bytes): {length_bytes}"
    )
    logging.info(log_entry)

if __name__ == "__main__":
    # Test logging
    source_ip = "192.168.1.10"  # Replace with the actual source IP
    destination_ip = "192.168.1.20"  # Replace with the actual destination IP
    source_port = 12345  # Replace with the actual source port
    destination_port = 54321  # Replace with the actual destination port
    protocol = "UDP"
    communication_type = "Unicasted"  # Replace with "Multicast" or "Broadcast" as needed
    length_bytes = 100  # Replace with the actual length in bytes
    flags_hex = "0x0123"  # Replace with the actual flags in hex

    log_communication(
        source_ip, destination_ip, source_port, destination_port, protocol, communication_type, length_bytes
    )
