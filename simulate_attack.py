import socket
import time

TARGET = "127.0.0.1"
PORTS = {2222: 9, 3306: 6, 8080: 2}  # port: number of hits

for port, hits in PORTS.items():
    for _ in range(hits):
        try:
            s = socket.create_connection((TARGET, port), timeout=1)
            s.close()
        except Exception as e:
            print(f"Port {port} failed: {e}")
        time.sleep(0.2)
    print(f"Sent {hits} hits to port {port}")