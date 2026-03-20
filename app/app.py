from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="devopsdb",
        user="devops",
        password="devops"
    )
    return conn

@app.route("/")
def home():
    return "DevOps App is running!"

@app.route("/data", methods=["POST"])
def add_data():
    content = request.json.get("content")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO messages (content) VALUES (%s)", (content,))
    conn.commit()

    cur.close()
    conn.close()

    return {"status": "saved"}

@app.route("/data", methods=["GET"])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM messages")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
