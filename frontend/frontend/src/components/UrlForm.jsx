import { useState } from "react";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import RefreshIcon from "@mui/icons-material/Refresh";

function UrlForm() {
  const [url, setUrl] = useState("");
  const [customCode, setCustomCode] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setError("");
    setShortUrl("");
    setCopied(false);

    try {
      const response = await fetch("https://canine-easiness-upheld.ngrok-free.dev/shorten", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          url: url,
          custom_code: customCode,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setShortUrl(data.short_url);
      } else {
        setError(data.error || "Something went wrong");
      }
    } catch (err) {
      setError("Server connection failed");
    }
  };

  const handleReset = () => {
    setUrl("");
    setCustomCode("");
    setShortUrl("");
    setError("");
    setCopied(false);
  };

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(shortUrl);
      setCopied(true);
    } catch (err) {
      setError("Failed to copy URL");
    }
  };

  return (
    <div className="form-card">
      <form onSubmit={handleSubmit}>
        {/* URL INPUT */}

        <div className="input-group">
          <label>DESTINATION URL</label>

          <input
            type="text"
            placeholder="https://example.com/very-long-link"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
          />
        </div>

        {/* CUSTOM CODE */}

        <div className="input-group">
          <label>CUSTOM ALIAS (OPTIONAL)</label>

          <input
            type="text"
            placeholder="e.g. my-portfolio"
            value={customCode}
            onChange={(e) => setCustomCode(e.target.value)}
          />
        </div>

        {/* BUTTONS */}

        <div className="button-group">
          <button type="submit" className="btn-primary">
            Shorten Now
          </button>

          <button type="button" onClick={handleReset} className="btn-reset">
            <RefreshIcon fontSize="small" />
            Reset Fields
          </button>
        </div>
      </form>

      {/* ERROR */}

      {error && <p className="error-text">⚠ {error}</p>}

      {/* RESULT */}

      {shortUrl && (
        <div className="result-box">
          <p className="result-label">SUCCESSFULLY SHORTENED:</p>

          <a href={shortUrl} target="_blank" rel="noreferrer">
            {shortUrl}
          </a>

          <button onClick={handleCopy} className="copy-btn">
            <ContentCopyIcon fontSize="small" />

            {copied ? "Copied!" : "Copy"}
          </button>
        </div>
      )}
    </div>
  );
}

export default UrlForm;
