import socket


def send_udp_message(message, address, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), (address, port))
    udp_socket.close()


# send_udp_message("Test Nachricht", "127.0.0.1", 8000)
send_udp_message("Test Nachricht", "192.168.178.20", 8000)
