from flask import Flask
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        return f"DB Connected: {result} 🎉"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)