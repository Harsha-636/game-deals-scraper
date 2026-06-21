# 🎮 GameDeals — AI-Powered Game Price Scraper & Dashboard

> A full-stack web application that scrapes real-time game deals from Steam, displays them in a modern dashboard with filters, and uses **Claude AI** to analyze and recommend the best buys.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com)
[![Claude AI](https://img.shields.io/badge/Claude-AI%20Powered-purple.svg)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 🔍 **Real-time Scraping** | Pulls live deals from SteamSpy API + BeautifulSoup fallback |
| 🤖 **AI Deal Analysis** | Claude AI picks Top Deal, Budget Pick & Hidden Gem with reasoning |
| 🎛️ **Filters** | Genre, max price, quick filters (75%+ off, under $5, etc.) |
| 📊 **Dashboard Stats** | Total deals, avg discount, best deal, cheapest game |
| ⚡ **Caching** | 5-min server-side cache to avoid hammering APIs |
| 🎨 **Modern UI** | Dark gaming aesthetic, animated marquee, responsive design |
| 🚀 **Deployable** | Render/Railway-ready with Procfile and Gunicorn |

---

## 🛠️ Tech Stack

**Backend**
- Python 3.11+
- Flask (REST API + templating)
- BeautifulSoup4 (HTML scraping)
- Requests (HTTP client)
- Anthropic Claude API (AI analysis)

**Frontend**
- Vanilla JS (no framework bloat)
- CSS custom properties + animations
- Google Fonts (Syne + Space Grotesk)
- Fully responsive

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Harsha-636/game-deals-scraper.git
cd game-deals-scraper
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 5. Run the app
```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) 🎮

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard |
| `/api/games` | GET | All deals (supports `?genre=`, `?max_price=`, `?sort_by=`) |
| `/api/ai-picks` | GET | Claude AI deal analysis |
| `/api/genres` | GET | All available genres |
| `/api/stats` | GET | Market overview stats |

---

## ☁️ Deploy to Render (Free)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set **Build Command**: `pip install -r requirements.txt`
5. Set **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
6. Add environment variable: `ANTHROPIC_API_KEY=your_key`
7. Deploy!

---

## 📁 Project Structure

```
game-deals-scraper/
├── app.py                  # Flask app + API routes
├── scraper/
│   ├── scraper.py          # Web scraping logic (SteamSpy API + BeautifulSoup)
│   └── ai_analyzer.py      # Claude AI deal analysis
├── templates/
│   └── index.html          # Main dashboard template
├── static/
│   ├── css/style.css       # Dark gaming UI styles
│   └── js/main.js          # Frontend interactivity
├── requirements.txt
├── Procfile                # For Render/Railway deployment
└── .env.example
```

---

## 🤖 How the AI Works

The `/api/ai-picks` endpoint sends the top 10 deals to Claude API with a structured prompt. Claude returns JSON with:
- **Top Pick** — best overall value
- **Budget Pick** — best deal under $10
- **Hidden Gem** — underrated title
- **Market Summary** — analysis of the current sale season

```python
# ai_analyzer.py
def analyze_deals(games):
    prompt = f"Analyze these deals and return JSON: {games_summary}"
    response = claude_api.call(prompt)
    return parse_json(response)
```

---

## 👨‍💻 Author

**Sai Harsha Vardhan Reddy Avula**  
B.Tech CSE @ KMCE Hyderabad (2027)  
Java Developer · Full Stack · AI/ML

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/harsha-avula)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/Harsha-636)

---

## 📄 License

MIT License — feel free to use and modify!
