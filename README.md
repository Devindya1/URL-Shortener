📌 URL Shortener (Full Stack Web App)
🚀 Overview

A full-stack URL shortener web application built using Flask (Python), React, and MySQL.
It allows users to convert long URLs into short, shareable links with optional custom aliases.

✨ Features
- 🔗 Shorten long URLs instantly
- ✏️ Custom alias support (optional)
- 📊 Click tracking (stored in database)
- ⚡ Fast redirect system
- 🌐 Public API exposure via deployment
- 🎨 Clean and responsive UI
- 🧱 Tech Stack

Frontend:

- React
- JavaScript
- HTML/CSS

Backend:

- Flask (Python)
- Flask-CORS
- Gunicorn (for deployment)

Database:

- MySQL

Tools:

- Ngrok (development testing)
- Git & GitHub

⚙️ How It Works
1. User enters a long URL in the frontend
2. React sends request to Flask API
3. Flask generates a unique short code
4. Data is stored in MySQL database
5. Short URL is returned to frontend
6. When accessed, backend redirects to original URL

▶️ How to Run Locally
Backend

- cd backend
- pip install -r requirements.txt
- python app.py

Frontend

- cd frontend
- npm install
- npm run dev

Live demostration

https://github.com/user-attachments/assets/143b47a5-598c-49fa-8e95-0a021b65b769


🧠 Key Learnings
- REST API development with Flask
- Frontend-backend integration
- Database design and queries
- Handling CORS issues
- Deploying backend services
  
🚀 Future Improvements
- QR code generation
- Analytics dashboard
- User authentication
- URL expiration feature
- Advanced click tracking
  
👨‍💻 Author

Built by L. Devindya Senavirathne
  
