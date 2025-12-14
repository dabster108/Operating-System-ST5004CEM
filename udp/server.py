import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP server listening on", UDP_IP, "port", UDP_PORT)

while True:
    data, addr = sock.recvfrom(1024)
    print("Received data:", data)
    message = data.decode()
    print("Decoded message:", message)
    print("From:", addr)