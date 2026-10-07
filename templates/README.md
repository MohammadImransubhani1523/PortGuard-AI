# Port Guard AI – Smart Vulnerability & Threat Scanner

A network security tool that scans ports, uses honeypot listeners to catch
unauthorized connections, calculates risk scores, and shows everything on a
real-time Flask dashboard.

## Features
- Socket-based port scanner for normal service ports
- Honeypot listener on trap ports (2222, 3306, 8080, 2121, 2323) that logs attacker IP and port
- Risk scoring: risk = min(10, hits x 2) -> Low Threat / Suspicious / MALICIOUS
- Flask + Chart.js dashboard with color-coded table and bar chart
- SQLite storage for scan results and honeypot logs

## Tech Stack
Python, Flask, SQLite, HTML, CSS, JavaScript, Chart.js

## How to Run
pip install flask

1. Terminal 1: python monitor.py
2. Terminal 2: python dashboard.py  (open http://127.0.0.1:5000)
3. Terminal 3: python simulate_attack.py

## Screenshots
![Dashboard](screenshots/dashboard.png)

## Future Scope
ML-based anomaly detection, email/SMS alerts, PDF reports.

## Authors
E. Mohitha, Md. Imran Subhani, R. Tejaswi, A. Vamsi Venkata Hari Krishna
SRK Institute of Technology, Vijayawada (JNTU Kakinada), 2026