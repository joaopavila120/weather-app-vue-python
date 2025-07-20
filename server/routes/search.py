from flask import Blueprint, request, jsonify, current_app
import requests
from extensions import cache, limiter

search_bp = Blueprint('search', __name__)
GEO_URL   = 'https://api.openweathermap.org/geo/1.0/direct'

@search_bp.route('/search')
@limiter.limit("30 per minute")
@cache.cached(timeout=300, query_string=True)
def search_cities():
    q = request.args.get('city')
    if not q:
        return jsonify({'error': 'Missing "city" parameter.'}), 400

    #asking for more results 
    resp = requests.get(GEO_URL, params={
        'q': q,
        'limit': 10,
        'appid': current_app.config['OPENWEATHER_KEY']
    })
    try:
        resp.raise_for_status()
    except requests.HTTPError:
        return jsonify({'error': 'Error fetching geocoding data.'}), resp.status_code

    raw = resp.json()
    unique = []
    seen  = set()

    # to not repeat the matches
    for item in raw:
        key = (item.get('name'), item.get('country'))
        if key not in seen:
            seen.add(key)
            unique.append(item)
        if len(unique) >= 5:
            break

    return jsonify(unique)
