import socket


def listen_udp(port):
    # Socket erstellen
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Socket an eine Adresse und einen Port binden
    udp_socket.bind(("0.0.0.0", port))

    print(f"Listening for UDP messages on port {port}...")

    try:
        while True:
            # Nachrichten empfangen (maximal 1024 Bytes)
            data, addr = udp_socket.recvfrom(1024)
            print(f"Received message from {addr}: {data}")
    except KeyboardInterrupt:
        print("\nStopping the listener.")
    finally:
        udp_socket.close()


# Auf Port 8000 lauschen
listen_udp(8000)
