from flask import Flask, render_template, request, redirect, url_for
from db import init_db, get_connection

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    status = request.args.get("status", "all")  # all, active, completed

    conn = get_connection()
    cur = conn.cursor()

    # Counts
    cur.execute("SELECT COUNT(*) AS total FROM tasks;")
    total = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS active FROM tasks WHERE completed = 0;")
    active = cur.fetchone()["active"]

    cur.execute("SELECT COUNT(*) AS done FROM tasks WHERE completed = 1;")
    done = cur.fetchone()["done"]

    # Filtered list
    if status == "active":
        cur.execute("SELECT * FROM tasks WHERE completed = 0 ORDER BY id DESC;")
    elif status == "completed":
        cur.execute("SELECT * FROM tasks WHERE completed = 1 ORDER BY id DESC;")
    else:
        cur.execute("SELECT * FROM tasks ORDER BY completed, id DESC;")

    tasks = cur.fetchall()
    conn.close()

    return render_template(
        "index.html",
        tasks=tasks,
        status=status,
        total=total,
        active=active,
        done=done
    )

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    due_date = request.form.get("due_date", "").strip()

    if title == "":
        return redirect(url_for("home"))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title, due_date) VALUES (?, ?);",
        (title, due_date if due_date else None)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

@app.route("/uncomplete/<int:task_id>", methods=["POST"])
def uncomplete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET completed = 0 WHERE id = ?;", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home", status=request.args.get("status", "all")))

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET completed = 1 WHERE id = ?;", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home", status=request.args.get("status", "all")))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?;", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)