import requests
import random
import time

_cache = {'data': None, 'time': 0}
CACHE_DURATION = 300

MOCK_GAMES = [
    {"id": 1, "title": "Elden Ring", "genre": "RPG", "original_price": 59.99, "sale_price": 29.99, "discount_pct": 50, "rating": 9.6, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1245620/header.jpg", "url": "https://store.steampowered.com/app/1245620", "reviews": "Overwhelmingly Positive", "badge": "🔥 Hot Deal"},
    {"id": 2, "title": "Cyberpunk 2077", "genre": "RPG", "original_price": 59.99, "sale_price": 17.99, "discount_pct": 70, "rating": 8.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1091500/header.jpg", "url": "https://store.steampowered.com/app/1091500", "reviews": "Very Positive", "badge": "💎 Best Value"},
    {"id": 3, "title": "The Witcher 3", "genre": "RPG", "original_price": 39.99, "sale_price": 7.99, "discount_pct": 80, "rating": 9.5, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/292030/header.jpg", "url": "https://store.steampowered.com/app/292030", "reviews": "Overwhelmingly Positive", "badge": "🏆 All-Time Classic"},
    {"id": 4, "title": "Hades", "genre": "Roguelike", "original_price": 24.99, "sale_price": 9.99, "discount_pct": 60, "rating": 9.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1145360/header.jpg", "url": "https://store.steampowered.com/app/1145360", "reviews": "Overwhelmingly Positive", "badge": "🎯 Editor's Pick"},
    {"id": 5, "title": "Hollow Knight", "genre": "Platformer", "original_price": 14.99, "sale_price": 5.24, "discount_pct": 65, "rating": 9.7, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/367520/header.jpg", "url": "https://store.steampowered.com/app/367520", "reviews": "Overwhelmingly Positive", "badge": "💎 Best Value"},
    {"id": 6, "title": "Stardew Valley", "genre": "Simulation", "original_price": 14.99, "sale_price": 7.49, "discount_pct": 50, "rating": 9.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg", "url": "https://store.steampowered.com/app/413150", "reviews": "Overwhelmingly Positive", "badge": "🌟 Fan Favorite"},
    {"id": 7, "title": "Dark Souls III", "genre": "Action RPG", "original_price": 59.99, "sale_price": 11.99, "discount_pct": 80, "rating": 9.2, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/374320/header.jpg", "url": "https://store.steampowered.com/app/374320", "reviews": "Very Positive", "badge": "🔥 Hot Deal"},
    {"id": 8, "title": "Celeste", "genre": "Platformer", "original_price": 19.99, "sale_price": 3.99, "discount_pct": 80, "rating": 9.7, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/504230/header.jpg", "url": "https://store.steampowered.com/app/504230", "reviews": "Overwhelmingly Positive", "badge": "🎯 Editor's Pick"},
    {"id": 9, "title": "Terraria", "genre": "Sandbox", "original_price": 9.99, "sale_price": 2.49, "discount_pct": 75, "rating": 9.8, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg", "url": "https://store.steampowered.com/app/105600", "reviews": "Overwhelmingly Positive", "badge": "💎 Best Value"},
    {"id": 10, "title": "Doom Eternal", "genre": "FPS", "original_price": 39.99, "sale_price": 9.99, "discount_pct": 75, "rating": 9.2, "platform": "Steam", "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/782330/header.jpg", "url": "https://store.steampowered.com/app/782330", "reviews": "Very Positive", "badge": "💥 Action Packed"},
]

def scrape_games():
    global _cache
    now = time.time()
    if _cache['data'] and (now - _cache['time']) < CACHE_DURATION:
        return _cache['data']
    games = _get_enriched_mock()
    _cache['data'] = games
    _cache['time'] = now
    return games

def _get_enriched_mock():
    games = []
    for g in MOCK_GAMES:
        g2 = g.copy()
        g2['sale_price'] = round(g['sale_price'] * random.uniform(0.95, 1.05), 2)
        games.append(g2)
    return games
