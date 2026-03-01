from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from functools import wraps
from detection import analyze_logs

app = Flask(__name__)
app.secret_key = "sentinelx_ultra_secure_key"



def get_db():
    conn = sqlite3.connect("sentinelx.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        severity TEXT,
        details TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper



@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid Credentials")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        try:
            conn = get_db()
            conn.execute(
                "INSERT INTO users (username,password) VALUES (?,?)",
                (username, password)
            )
            conn.commit()
            conn.close()

            flash("Account Created Successfully")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            flash("User already exists")

    return render_template("signup.html")


@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        username = request.form["username"]
        new_password = generate_password_hash(request.form["password"])

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()

        if user:
            conn.execute(
                "UPDATE users SET password=? WHERE username=?",
                (new_password, username)
            )
            conn.commit()
            conn.close()

            flash("Password Updated Successfully")
            return redirect(url_for("login"))
        else:
            flash("User Not Found")

    return render_template("forgot_password.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():

    alerts = analyze_logs()
    conn = get_db()

    for alert in alerts:
        existing = conn.execute("""
            SELECT * FROM alerts
            WHERE title=? AND details=? AND status='Open'
        """, (alert["title"], alert["details"])).fetchone()

        if not existing:
            conn.execute("""
                INSERT INTO alerts (title,severity,details,status)
                VALUES (?,?,?,?)
            """, (
                alert["title"],
                alert["severity"],
                alert["details"],
                "Open"
            ))

    conn.commit()

    open_alerts = conn.execute(
        "SELECT * FROM alerts WHERE status='Open'"
    ).fetchall()

    closed_alerts = conn.execute(
        "SELECT * FROM alerts WHERE status='Closed'"
    ).fetchall()

    conn.close()

    high = sum(1 for a in open_alerts if a["severity"] == "High")
    medium = sum(1 for a in open_alerts if a["severity"] == "Medium")
    low = sum(1 for a in open_alerts if a["severity"] == "Low")

    return render_template(
        "dashboard.html",
        open_count=len(open_alerts),
        closed_count=len(closed_alerts),
        high=high,
        medium=medium,
        low=low
    )


@app.route("/open_alerts")
@login_required
def view_open_alerts():
    conn = get_db()
    alerts = conn.execute(
        "SELECT * FROM alerts WHERE status='Open'"
    ).fetchall()
    conn.close()

    return render_template("open_alerts.html", alerts=alerts)


@app.route("/closed_alerts")
@login_required
def view_closed_alerts():
    conn = get_db()
    alerts = conn.execute(
        "SELECT * FROM alerts WHERE status='Closed'"
    ).fetchall()
    conn.close()

    return render_template("closed_alerts.html", alerts=alerts)


@app.route("/close/<int:alert_id>")
@login_required
def close_alert(alert_id):
    conn = get_db()
    conn.execute(
        "UPDATE alerts SET status='Closed' WHERE id=?",
        (alert_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("view_open_alerts"))




if __name__ == "__main__":
    app.run(debug=True)