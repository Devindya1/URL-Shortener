from flask import Flask, request, jsonify, redirect
from db import get_db_connection
import string
import random

app = Flask(__name__)  


#  Generate short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


#  Home route (test DB)
@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        return f"DB Connected: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


#  Shorten URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # handle duplicate short codes (retry logic)
        for _ in range(5):
            short_code = generate_code()
            try:
                cursor.execute(
                    "INSERT INTO urls (original_url, short_code) VALUES (%s, %s)",
                    (original_url, short_code)
                )
                conn.commit()
                break
            except:
                continue

        conn.close()

        short_url = request.host_url + short_code

        return jsonify({"short_url": short_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


#  Redirect (we'll properly use this on Day 3, but adding now is fine)
@app.route('/<short_code>')
def redirect_url(short_code):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT original_url, clicks FROM urls WHERE short_code = %s",
            (short_code,)
        )
        result = cursor.fetchone()

        if result:
            # increment clicks
            cursor.execute(
                "UPDATE urls SET clicks = clicks + 1 WHERE short_code = %s",
                (short_code,)
            )
            conn.commit()
            conn.close()

            return redirect(result['original_url'])
        else:
            conn.close()
            return "URL not found", 404

    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)