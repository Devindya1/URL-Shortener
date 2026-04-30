Create database url_short;
use url_short;

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(10) UNIQUE,
    clicks INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);