function urlResult({ shortUrl }) {
  return (
    <div className="result-box">
      <h3>Shortened URL</h3>

      <a
        href={shortUrl}
        target="_blank"
        rel="noreferrer"
      >
        {shortUrl}
      </a>
    </div>
  );
}

export default urlResult;