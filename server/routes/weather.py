from flask import Blueprint, request, jsonify, current_app
import requests
from extensions import cache, limiter

weather_bp = Blueprint('weather', __name__)
BASE_URL   = 'https://api.openweathermap.org/data/2.5'

#request to OpenWeatherMap API.
    #Adds API key and metric units handles HTTP errors.

def proxy_request(path, params):
    params.update({
        'appid': current_app.config['OPENWEATHER_KEY'],
        'units': 'metric'
    })
    resp = requests.get(f"{BASE_URL}/{path}", params=params)
    try:
        resp.raise_for_status()
    except requests.HTTPError:
        # error message from OWM or generic text
        return None, resp.status_code, resp.json().get('message', resp.text)
    return resp.json(), 200, None

@weather_bp.route('/weather')
@limiter.limit("50 per hour")
@cache.cached(timeout=600, query_string=True)
def get_weather():
   # current weather by city name or latitude/longitude
    city = request.args.get('city')
    lat  = request.args.get('lat')
    lon  = request.args.get('lon')

    if city:
        params = {'q': city}
    elif lat and lon:
        params = {'lat': lat, 'lon': lon}
    else:
        return jsonify({'error': 'Missing "city" or "lat" & "lon" parameters.'}), 400

    data, status, err = proxy_request('weather', params)
    if status != 200:
        return jsonify({'error': err}), status
    return jsonify(data)

@weather_bp.route('/forecast')
@limiter.limit("50 per hour")
@cache.cached(timeout=600, query_string=True)
def get_forecast():
    """Get 5‑day/3‑hour forecast by city name or latitude/longitude."""
    city = request.args.get('city')
    lat  = request.args.get('lat')
    lon  = request.args.get('lon')

    if city:
        params = {'q': city}
    elif lat and lon:
        params = {'lat': lat, 'lon': lon}
    else:
        return jsonify({'error': 'Missing "city" or "lat" & "lon" parameters.'}), 400

    data, status, err = proxy_request('forecast', params)
    if status != 200:
        return jsonify({'error': err}), status
    return jsonify(data)
