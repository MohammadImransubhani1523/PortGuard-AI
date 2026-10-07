import socket

from db import get_db, init_db

NORMAL_PORTS = [22, 80, 443, 5000]


def calculate_risk(hits):
    risk = min(10, hits * 2)
    if risk >= 8:
        activity = "MALICIOUS ACTIVITY"
    elif risk >= 4:
        activity = "Suspicious Activity"
    else:
        activity = "Low Threat"
    return activity, risk


def scan_normal_ports(host="127.0.0.1"):
    found = []
    for port in NORMAL_PORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((host, port)) == 0:
            found.append(port)
        s.close()
    return found


def run_scan(host="127.0.0.1"):
    init_db()
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM open_ports")

    for port in scan_normal_ports(host):
        cur.execute(
            "INSERT INTO open_ports VALUES (?, ?, ?, ?)",
            (port, "Normal Service", 1, "Localhost"),
        )

    cur.execute("SELECT port, ip, COUNT(*) FROM honeypot_logs GROUP BY port, ip")
    for port, ip, hits in cur.fetchall():
        activity, risk = calculate_risk(hits)
        cur.execute(
            "INSERT INTO open_ports VALUES (?, ?, ?, ?)",
            (port, activity, risk, ip),
        )

    conn.commit()
    conn.close()
    print("[SCAN] Scan complete, results updated.")


if __name__ == "__main__":
    run_scan()