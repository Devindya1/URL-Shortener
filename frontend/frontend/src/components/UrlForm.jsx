import { useState } from "react";
import { shortenUrl } from "../services/api";

function UrlForm() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = await shortenUrl(url);

    if (data.short_url) {
      setShortUrl(data.short_url);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button type="submit">
          Shorten
        </button>
      </form>

      {shortUrl && (
        <p>
          Short URL:
          <a href={shortUrl} target="_blank">
            {shortUrl}
          </a>
        </p>
      )}
    </div>
  );
}

export default UrlForm;