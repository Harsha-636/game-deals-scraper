import json

def analyze_deals(games):
    if not games:
        return _fallback_analysis(games)
    return _fallback_analysis(games)

def _fallback_analysis(games):
    if not games:
        return {"headline": "No deals available.", "top_pick": {}, "budget_pick": {}, "hidden_gem": {}, "market_summary": ""}
    best = max(games, key=lambda x: x['discount_pct'])
    budget = min((g for g in games if g['sale_price'] < 15), key=lambda x: x['sale_price'], default=games[0])
    rated = max(games, key=lambda x: x['rating'])
    return {
        "headline": f"🔥 Up to {max(g['discount_pct'] for g in games)}% off — great time to grab some classics!",
        "top_pick": {
            "title": best['title'],
            "reason": f"At {best['discount_pct']}% off, this is the deepest discount available. A must-buy if you haven't played it.",
            "value_score": 9.0
        },
        "budget_pick": {
            "title": budget['title'],
            "reason": f"Under $15 and rated {budget['rating']}/10 — incredible value for budget-conscious gamers.",
            "value_score": 8.5
        },
        "hidden_gem": {
            "title": rated['title'],
            "reason": f"Rated {rated['rating']}/10 — consistently overlooked but an absolute masterpiece.",
            "value_score": rated['rating']
        },
        "market_summary": "Strong discounts across genres. Roguelikes and RPGs are seeing the deepest cuts right now."
    }
