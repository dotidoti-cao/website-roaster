"""
Website Roaster API
====================
Flask API that roasts any website using GLM-4 (智谱 AI).
Takes a URL, fetches the page, and generates a savage roast.

POST /api/roast
    Body: {"url": "https://example.com"}
    Response: {"roast": "...", "url": "...", "title": "..."}

Environment variables:
    ZHIPU_API_KEY: Your GLM-4 API key from https://open.bigmodel.cn/
"""

import os
import re
import time
import json
import logging
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("website-roaster")

ZHIPU_API_KEY = os.environ.get("ZHIPU_API_KEY", "")
ZHIPU_API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# HTTP headers that look like a normal browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def fetch_page(url: str, timeout: int = 15) -> dict:
    """Fetch a webpage and extract text + metadata."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
    except requests.RequestException as e:
        logger.warning("Failed to fetch %s: %s", url, e)
        return {"error": f"Failed to fetch the website: {e}"}

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove script / style / nav / footer noise
    for tag in soup(["script", "style", "nav", "footer", "noscript", "iframe"]):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else ""
    meta_desc = ""
    for meta in soup.find_all("meta"):
        if meta.get("name", "").lower() == "description":
            meta_desc = meta.get("content", "")
            break

    # Grab visible text (limit to ~6000 chars to keep prompt sane)
    body = soup.body
    text = body.get_text(separator=" ", strip=True) if body else ""
    text = re.sub(r"\s+", " ", text).strip()[:6000]

    return {
        "title": title,
        "description": meta_desc,
        "text": text,
        "url": resp.url,
        "status_code": resp.status_code,
    }


def call_glm4(prompt: str) -> str:
    """Call GLM-4 to generate a roast."""
    if not ZHIPU_API_KEY:
        return (
            "⚠️ API key not configured. Set the ZHIPU_API_KEY environment variable "
            "and restart the server. Get your key at https://open.bigmodel.cn/"
        )

    payload = {
        "model": "glm-4-flash",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Website Roaster — a savage, witty AI that roasts "
                    "websites with hilarious, sharp humor. You are like a "
                    "stand-up comedian who audits websites. Be brutally honest, "
                    "funny, and creative. Use emojis sparingly for punch. "
                    "Roast everything: design, UX, copy, tech stack, SEO, "
                    "performance vibes. Keep it under 300 words. Make people "
                    "laugh out loud. Write in English."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.9,
        "max_tokens": 600,
    }

    try:
        resp = requests.post(
            ZHIPU_API_URL,
            headers={
                "Authorization": f"Bearer {ZHIPU_API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.RequestException as e:
        logger.error("GLM-4 API error: %s", e)
        return f"🔥 The AI roaster is taking a coffee break. Try again in a moment! (Error: {e})"
    except (KeyError, IndexError) as e:
        logger.error("GLM-4 unexpected response: %s", resp.text[:500])
        return "🤖 The AI got roasted itself. Please try again!"


def build_prompt(page_data: dict) -> str:
    """Build the roast prompt from scraped page data."""
    title = page_data.get("title", "Unknown")
    desc = page_data.get("description", "")
    text = page_data.get("text", "")
    domain = urlparse(page_data.get("url", "")).netloc

    prompt = f"Roast this website:\n\nURL: {page_data.get('url', 'N/A')}\nDomain: {domain}\nTitle: {title}\nMeta Description: {desc}\n\nPage Content Sample:\n{text[:4000]}\n\nGive a hilarious, savage roast of this website. Be brutal but funny. Mention specific things from the content if possible."
    return prompt


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/api/roast", methods=["POST"])
def roast():
    """Roast a website."""
    data = request.get_json(silent=True) or {}
    url = (data.get("url") or "").strip()

    if not url:
        return jsonify({"error": "Missing 'url' field. Send a JSON body: {\"url\": \"https://...\"}"}), 400

    # Basic URL validation
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)
    if not parsed.netloc:
        return jsonify({"error": f"Invalid URL: {url}"}), 400

    logger.info("Roasting: %s", url)

    # 1. Fetch page
    page_data = fetch_page(url)
    if "error" in page_data:
        return jsonify(page_data), 502

    # 2. Generate roast via GLM-4
    prompt = build_prompt(page_data)
    roast_text = call_glm4(prompt)

    return jsonify({
        "roast": roast_text,
        "url": page_data.get("url", url),
        "title": page_data.get("title", ""),
        "description": page_data.get("description", ""),
    })


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "Website Roaster API"})


@app.route("/")
def index():
    return jsonify({
        "name": "Website Roaster API",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/roast": "Roast a website (body: {\"url\": \"...\"})",
            "GET /api/health": "Health check",
        },
        "demo": "https://tools.pojudao.com/roast.html",
        "docs": "https://github.com/austincao/website-roaster",
    })


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    logger.info("Starting Website Roaster API on port %d", port)
    app.run(host="0.0.0.0", port=port, debug=debug)
