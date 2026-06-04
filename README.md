<p align="center">
  <img src="https://raw.githubusercontent.com/austincao/website-roaster/main/assets/banner.png" alt="Website Roaster Banner" width="600">
</p>

<h1 align="center">🔥 Website Roaster — AI That Roasts Any Website</h1>

<p align="center">
  <strong>Drop a URL. Get brutally roasted by AI. No mercy. 100% hilarious.</strong>
</p>

<p align="center">
  <a href="https://tools.pojudao.com/roast.html"><strong>🔗 Try it Live — Free Demo</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/austincao/website-roaster/stargazers"><strong>⭐ Star This Repo</strong></a>
  &nbsp;·&nbsp;
  <a href="https://paypal.me/austincao8624/19"><strong>💳 Get Full Report ($19)</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/python-3.9+-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/status-production-brightgreen" alt="Production Ready">
  <img src="https://img.shields.io/badge/roasts-savage-red" alt="Roasts are savage">
</p>

---

## 🤔 What Is This?

**Website Roaster** is an AI-powered tool that takes any website URL and generates a hilarious, brutally honest roast. Think of it as a stand-up comedian doing a code review — but funnier, meaner, and somehow more accurate.

Paste your competitor's site, your own site, or your boss's startup landing page. Watch the AI tear it apart with savage precision.

### ✨ Features

- 🔥 **AI-Powered Roasts** — Uses GLM-4 (智谱 AI) to generate sharp, witty critiques
- 🌐 **Works on Any Website** — Paste any URL, public or private
- 🎨 **Sleek Dark Theme UI** — Single-file HTML, works offline, GitHub Pages ready
- ⚡ **Fast & Free Preview** — Get a taste of the roast instantly
- 📊 **Full Report ($19)** — In-depth multi-page audit: design, UX, SEO, copy, tech stack
- 🐍 **Simple Flask API** — Self-host in 5 minutes
- 📋 **Shareable** — Tweet your roast or copy a share link

<p align="center">
  <em>[ Demo Screenshot — paste a URL, get roasted ]</em>
</p>

---

## 🚀 Try It Now

**[👉 tools.pojudao.com/roast.html](https://tools.pojudao.com/roast.html)**

No sign-up. No download. Just paste a URL and watch the magic happen.

---

## 📦 Quick Start (Self-Host)

### Prerequisites

- Python 3.9+
- A [Zhipu AI API key](https://open.bigmodel.cn/) (free tier available)

### 1. Clone the repo

```bash
git clone https://github.com/austincao/website-roaster.git
cd website-roaster
```

### 2. Install dependencies

```bash
pip install flask flask-cors requests beautifulsoup4
```

### 3. Set your API key

```bash
export ZHIPU_API_KEY="your-api-key-here"
```

### 4. Run the API

```bash
python api/roast.py
```

The API will start on `http://localhost:5000`.

### 5. Open the frontend

Open `index.html` in your browser. If you're running the API locally, update the `API_URL` in `index.html`:

```javascript
const API_URL = "http://localhost:5000/api/roast";
```

---

## 📡 API Documentation

### `POST /api/roast`

Roast a website. Returns a savage AI-generated critique.

**Request:**

```json
{
  "url": "https://example.com"
}
```

**Response:**

```json
{
  "roast": "This website looks like it was designed by someone who just discovered <marquee> in 1998...",
  "url": "https://example.com",
  "title": "Example Domain",
  "description": "This domain is for use in illustrative examples..."
}
```

**cURL example:**

```bash
curl -X POST https://tools.pojudao.com/api/roast \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### `GET /api/health`

Health check. Returns `{"status": "ok"}`.

---

## 🗂 Project Structure

```
website-roaster/
├── index.html          # Single-file frontend (dark theme, offline-capable)
├── api/
│   └── roast.py        # Flask API (GLM-4 powered)
├── LICENSE             # MIT License
├── README.md           # You're reading it
└── .github/
    └── FUNDING.yml     # Sponsor links
```

---

## 💰 Get the Full Report — $19

The free preview gives you a hilarious 300-word roast. But if you want the **Full Roast Report**:

- 📄 Multi-page PDF with in-depth analysis
- 🎨 **Design critique** — color choices, spacing, accessibility
- 🧭 **UX audit** — navigation, CTAs, user flow
- 📝 **Copy review** — headlines, tone, grammar
- 🔍 **SEO basics** — meta tags, structure, performance vibes
- 🛠 **Tech stack roast** — what your HTML reveals about your choices

**[💳 Buy Full Report — $19 via PayPal](https://paypal.me/austincao8624/19)**

After payment, forward your receipt + the URL you want roasted. You'll get your full report within 24 hours.

---

## 🤝 Contributing

Pull requests are welcome! Want to make the roasts even more savage? Here's how:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/savage-mode`)
3. Commit your changes (`git commit -m 'Add extra sass'`)
4. Push to the branch (`git push origin feature/savage-mode`)
5. Open a Pull Request

---

## ⭐ Star History

If this project made you laugh, [give it a star ⭐](https://github.com/austincao/website-roaster/stargazers) — it helps more people discover it!

---

## 📄 License

MIT © [Austin Cao (曹春峰)](https://github.com/austincao)

---

## 🙏 Acknowledgments

- [GLM-4 by Zhipu AI](https://open.bigmodel.cn/) for powering the roasts
- [Flask](https://flask.palletsprojects.com/) for the lightweight API
- You, for having the courage to roast your own website

---

<br>

---

## 🔥 中文说明

### Website Roaster — AI 网站吐槽工具

丢一个网址进来，AI 帮你无情吐槽这个网站。把你的网站、竞品网站、或者老板的创业项目丢进来，看 AI 如何精准吐槽。

### 在线体验

**[👉 tools.pojudao.com/roast.html](https://tools.pojudao.com/roast.html)**

### 快速自部署

```bash
git clone https://github.com/austincao/website-roaster.git
cd website-roaster
pip install flask flask-cors requests beautifulsoup4
export ZHIPU_API_KEY="你的智谱API密钥"
python api/roast.py
```

打开 `index.html` 即可使用。

### 完整吐槽报告 — $19

免费预览只有 300 字的搞笑吐槽。购买完整报告可获得：

- 📄 **多页 PDF 深度分析**
- 🎨 **设计点评** — 配色、间距、可访问性
- 🧭 **UX 审计** — 导航、CTA、用户流程
- 📝 **文案审查** — 标题、语气、语法
- 🔍 **SEO 基础** — 元标签、结构、性能
- 🛠 **技术栈吐槽** — HTML 暴露了你的技术选择

**[💳 购买完整报告 ($19)](https://paypal.me/austincao8624/19)**

---

<p align="center">
  <strong>If this project made you laugh, <a href="https://github.com/austincao/website-roaster">⭐ star it</a>!</strong>
  <br>
  <sub>Made with 🔥 by <a href="https://github.com/austincao">Austin Cao (曹春峰)</a></sub>
</p>
