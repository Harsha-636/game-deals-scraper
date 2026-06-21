from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json, os, random, time

app = Flask(__name__)
CORS(app)

_cache = {'data': None, 'time': 0}

MOCK_GAMES = [
    {"id": 1, "title": "Elden Ring", "genre": "RPG", "original_price": 59.99, "sale_price": 29.99, "discount_pct": 50, "rating": 9.6, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1245620/header.jpg", "url": "https://store.steampowered.com/app/1245620", "reviews": "Overwhelmingly Positive", "badge": "🔥 Hot Deal"},
    {"id": 2, "title": "Cyberpunk 2077", "genre": "RPG", "original_price": 59.99, "sale_price": 17.99, "discount_pct": 70, "rating": 8.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1091500/header.jpg", "url": "https://store.steampowered.com/app/1091500", "reviews": "Very Positive", "badge": "💎 Best Value"},
    {"id": 3, "title": "The Witcher 3", "genre": "RPG", "original_price": 39.99, "sale_price": 7.99, "discount_pct": 80, "rating": 9.5, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/292030/header.jpg", "url": "https://store.steampowered.com/app/292030", "reviews": "Overwhelmingly Positive", "badge": "🏆 Classic"},
    {"id": 4, "title": "Hades", "genre": "Roguelike", "original_price": 24.99, "sale_price": 9.99, "discount_pct": 60, "rating": 9.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1145360/header.jpg", "url": "https://store.steampowered.com/app/1145360", "reviews": "Overwhelmingly Positive", "badge": "🎯 Pick"},
    {"id": 5, "title": "Hollow Knight", "genre": "Platformer", "original_price": 14.99, "sale_price": 5.24, "discount_pct": 65, "rating": 9.7, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/367520/header.jpg", "url": "https://store.steampowered.com/app/367520", "reviews": "Overwhelmingly Positive", "badge": "💎 Value"},
    {"id": 6, "title": "Stardew Valley", "genre": "Simulation", "original_price": 14.99, "sale_price": 7.49, "discount_pct": 50, "rating": 9.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg", "url": "https://store.steampowered.com/app/413150", "reviews": "Overwhelmingly Positive", "badge": "🌟 Favorite"},
    {"id": 7, "title": "Dark Souls III", "genre": "Action RPG", "original_price": 59.99, "sale_price": 11.99, "discount_pct": 80, "rating": 9.2, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/374320/header.jpg", "url": "https://store.steampowered.com/app/374320", "reviews": "Very Positive", "badge": "🔥 Hot"},
    {"id": 8, "title": "Celeste", "genre": "Platformer", "original_price": 19.99, "sale_price": 3.99, "discount_pct": 80, "rating": 9.7, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/504230/header.jpg", "url": "https://store.steampowered.com/app/504230", "reviews": "Overwhelmingly Positive", "badge": "🎯 Pick"},
    {"id": 9, "title": "Terraria", "genre": "Sandbox", "original_price": 9.99, "sale_price": 2.49, "discount_pct": 75, "rating": 9.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg", "url": "https://store.steampowered.com/app/105600", "reviews": "Overwhelmingly Positive", "badge": "💎 Value"},
    {"id": 10, "title": "Doom Eternal", "genre": "FPS", "original_price": 39.99, "sale_price": 9.99, "discount_pct": 75, "rating": 9.2, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/782330/header.jpg", "url": "https://store.steampowered.com/app/782330", "reviews": "Very Positive", "badge": "💥 Action"},
]

def get_games_data():
    global _cache
    now = time.time()
    if _cache['data'] and (now - _cache['time']) < 300:
        return _cache['data']
    games = []
    for g in MOCK_GAMES:
        g2 = g.copy()
        g2['sale_price'] = round(g['sale_price'] * random.uniform(0.95, 1.05), 2)
        games.append(g2)
    _cache['data'] = games
    _cache['time'] = now
    return games

def get_ai_analysis(games):
    best = max(games, key=lambda x: x['discount_pct'])
    budget = min((g for g in games if g['sale_price'] < 15), key=lambda x: x['sale_price'], default=games[0])
    rated = max(games, key=lambda x: x['rating'])
    return {
        "headline": f"Up to {max(g['discount_pct'] for g in games)}% off today!",
        "top_pick": {"title": best['title'], "reason": f"Deepest discount at {best['discount_pct']}% off.", "value_score": 9.0},
        "budget_pick": {"title": budget['title'], "reason": f"Under $15 and rated {budget['rating']}/10.", "value_score": 8.5},
        "hidden_gem": {"title": rated['title'], "reason": f"Rated {rated['rating']}/10 — a masterpiece.", "value_score": rated['rating']},
        "market_summary": "Strong discounts across all genres right now."
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/games')
def api_games():
    genre = request.args.get('genre', 'all')
    max_price = request.args.get('max_price', None)
    sort_by = request.args.get('sort_by', 'discount')
    games = get_games_data()
    if genre != 'all':
        games = [g for g in games if g['genre'].lower() == genre.lower()]
    if max_price:
        games = [g for g in games if g['sale_price'] <= float(max_price)]
    if sort_by == 'discount':
        games.sort(key=lambda x: x['discount_pct'], reverse=True)
    elif sort_by == 'price':
        games.sort(key=lambda x: x['sale_price'])
    elif sort_by == 'rating':
        games.sort(key=lambda x: x['rating'], reverse=True)
    return jsonify({'games': games, 'total': len(games)})

@app.route('/api/ai-picks')
def api_ai_picks():
    games = get_games_data()
    analysis = get_ai_analysis(games)
    return jsonify({'analysis': analysis, 'deals': games[:5]})

@app.route('/api/genres')
def api_genres():
    games = get_games_data()
    genres = list(set(g['genre'] for g in games))
    return jsonify({'genres': sorted(genres)})

@app.route('/api/stats')
def api_stats():
    games = get_games_data()
    if not games:
        return jsonify({})
    best_deal = max(games, key=lambda x: x['discount_pct'])
    cheapest = min(games, key=lambda x: x['sale_price'])
    return jsonify({
        'total_games': len(games),
        'avg_discount': round(sum(g['discount_pct'] for g in games) / len(games), 1),
        'best_deal': best_deal,
        'cheapest': cheapest
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
