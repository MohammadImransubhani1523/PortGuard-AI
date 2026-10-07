import time

from db import init_db
from honeypot_listener import start_honeypots
from scanner import run_scan

SCAN_INTERVAL = 10  # seconds

if __name__ == "__main__":
    print("[INFO] Initializing Port Guard AI Monitoring Engine...")
    init_db()
    start_honeypots()
    print("[SUCCESS] Monitoring started. Press CTRL+C to stop.")
    while True:
        run_scan()
        time.sleep(SCAN_INTERVAL)