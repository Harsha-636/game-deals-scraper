from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from scraper.scraper import scrape_games
from scraper.ai_analyzer import analyze_deals
import json, os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/games')
def get_games():
    genre = request.args.get('genre', 'all')
    max_price = request.args.get('max_price', None)
    sort_by = request.args.get('sort_by', 'discount')
    games = scrape_games()
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
def ai_picks():
    games = scrape_games()
    top_deals = sorted(games, key=lambda x: x['discount_pct'], reverse=True)[:10]
    analysis = analyze_deals(top_deals)
    return jsonify({'analysis': analysis, 'deals': top_deals[:5]})

@app.route('/api/genres')
def get_genres():
    games = scrape_games()
    genres = list(set(g['genre'] for g in games))
    return jsonify({'genres': sorted(genres)})

@app.route('/api/stats')
def get_stats():
    games = scrape_games()
    if not games:
        return jsonify({})
    avg_discount = sum(g['discount_pct'] for g in games) / len(games)
    best_deal = max(games, key=lambda x: x['discount_pct'])
    cheapest = min(games, key=lambda x: x['sale_price'])
    return jsonify({
        'total_games': len(games),
        'avg_discount': round(avg_discount, 1),
        'best_deal': best_deal,
        'cheapest': cheapest
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
