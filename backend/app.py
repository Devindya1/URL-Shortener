from flask import Flask, request, jsonify, redirect
from db import get_db_connection
import string
import random
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Validate URL
def is_valid_url(url):
    pattern = re.compile(
        r'^(https?:\/\/)?'
        r'([\w\-]+\.)+[\w\-]+'
        r'(\:[0-9]+)?(\/\S*)?$'
    )
    return re.match(pattern, url)


# Generate short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Home route
@app.route('/')
def home():
    return "URL Shortener API running"


# Shorten URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    custom_code = data.get('custom_code')

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check duplicate original URL
        cursor.execute(
            "SELECT short_code FROM urls WHERE original_url = %s",
            (original_url,)
        )
        existing = cursor.fetchone()

        if existing:
            conn.close()
            return jsonify({
                "short_url": request.host_url + existing[0],
                "message": "URL already shortened"
            })

        # Handle custom code
        if custom_code:
            short_code = custom_code

            cursor.execute(
                "SELECT id FROM urls WHERE short_code = %s",
                (short_code,)
            )
            if cursor.fetchone():
                conn.close()
                return jsonify({"error": "Custom code already in use"}), 400
        else:
            # Generate unique code
            for _ in range(5):
                short_code = generate_code()
                cursor.execute(
                    "SELECT id FROM urls WHERE short_code = %s",
                    (short_code,)
                )
                if not cursor.fetchone():
                    break

        # Insert into DB
        cursor.execute(
            "INSERT INTO urls (original_url, short_code) VALUES (%s, %s)",
            (original_url, short_code)
        )
        conn.commit()
        conn.close()

        return jsonify({
            "short_url": request.host_url + short_code
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Redirect
@app.route('/<short_code>')
def redirect_url(short_code):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT original_url FROM urls WHERE short_code = %s",
            (short_code,)
        )
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "UPDATE urls SET clicks = clicks + 1 WHERE short_code = %s",
                (short_code,)
            )
            conn.commit()
            conn.close()

            return redirect(result['original_url'])
        else:
            conn.close()
            return jsonify({"error": "URL not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)