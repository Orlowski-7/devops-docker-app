from flask import Flask, request, jsonify
import psycopg2
import time

app = Flask(__name__)

DB_CONFIG = {
    "host": "db",
    "database": "devopsdb",
    "user": "devops",
    "password": "devops"
}


def get_db_connection(retries=10, delay=2):
    last_error = None

    for attempt in range(retries):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            return conn
        except psycopg2.OperationalError as e:
            last_error = e
            print(f"[DB RETRY] Attempt {attempt + 1}/{retries} failed: {e}")
            time.sleep(delay)

    raise last_error


@app.route("/")
def home():
    return "DevOps App is running!"


@app.route("/health")
def health():
    try:
        conn = get_db_connection(retries=2, delay=1)
        conn.close()
        return {"status": "ok", "database": "connected"}, 200
    except Exception as e:
        return {"status": "error", "database": str(e)}, 500


@app.route("/data", methods=["POST"])
def add_data():
    data = request.get_json(silent=True) or {}
    content = data.get("content")

    if not content:
        return {"error": "content is required"}, 400

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO messages (content) VALUES (%s)", (content,))
    conn.commit()

    cur.close()
    conn.close()

    return {"status": "saved", "content": content}, 201


@app.route("/data", methods=["GET"])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, content FROM messages ORDER BY id ASC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    result = [{"id": row[0], "content": row[1]} for row in rows]
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)