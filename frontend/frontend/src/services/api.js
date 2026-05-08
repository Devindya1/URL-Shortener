const API_URL = "http://127.0.0.1:5000";

export const shortenUrl = async (originalUrl) => {
  const response = await fetch(`${API_URL}/shorten`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      original_url: originalUrl,
    }),
  });

  return response.json();
};