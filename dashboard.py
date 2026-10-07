from flask import Flask, render_template

from db import get_db, init_db

app = Flask(__name__)


@app.route("/")
def dashboard():
    init_db()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT port, activity, risk, source_ip FROM open_ports ORDER BY risk DESC")
    rows = cur.fetchall()
    conn.close()

    ports = [{"port": p, "activity": a, "risk": r, "ip": ip} for p, a, r, ip in rows]
    total_risk = sum(p["risk"] for p in ports)
    honeypots = sum(1 for p in ports if p["activity"] != "Normal Service")

    return render_template(
        "dashboard.html",
        ports=ports,
        open_ports=len(ports),
        total_risk=total_risk,
        honeypots=honeypots,
    )


if __name__ == "__main__":
    app.run(debug=True)