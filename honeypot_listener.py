import socket
import threading
import time

from db import get_db, init_db

HONEYPOT_PORTS = [2222, 3306, 8080, 2121, 2323]
THRESHOLD = 5


def log_hit(ip, port):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO honeypot_logs (ip, port) VALUES (?, ?)", (ip, port))
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM honeypot_logs WHERE port = ?", (port,))
    count = cur.fetchone()[0]
    conn.close()
    if count > THRESHOLD:
        print(f"MALICIOUS ACTIVITY -> Port {port} accessed {count} times (from {ip})")
    else:
        print(f"Normal Access -> Port {port} (Count: {count}) from {ip}")


def handle_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("0.0.0.0", port))
    except OSError as e:
        print(f"[WARN] Cannot bind port {port}: {e}")
        return
    sock.listen(5)
    while True:
        try:
            client, addr = sock.accept()
            log_hit(addr[0], port)
            client.close()
        except Exception as e:
            print(f"[ERROR] Port {port}: {e}")


def start_honeypots():
    init_db()
    print(f"Honeypot listening on ports: {HONEYPOT_PORTS}")
    for p in HONEYPOT_PORTS:
        threading.Thread(target=handle_port, args=(p,), daemon=True).start()


if __name__ == "__main__":
    start_honeypots()
    while True:
        time.sleep(1)