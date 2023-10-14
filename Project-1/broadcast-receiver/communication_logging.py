import logging

# Configure the logger
logging.basicConfig(filename='/app/communication.log', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger("communication_logging")

# Creates a log using information provided
def log_communication( source_ip, destination_ip, source_port, destination_port, protocol, communication_type, length_bytes):
    log_entry = (
        f"[{communication_type}] "
        f"Source IP: {source_ip}, Destination IP: {destination_ip}, "
        f"Source Port: {source_port}, Destination Port: {destination_port}, "
        f"Protocol: {protocol}, Length (Bytes): {length_bytes}"
    )
    logger.debug(log_entry)

