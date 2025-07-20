import os
from flask import Flask
from dotenv import load_dotenv

from config     import Config
from extensions import cors, cache, limiter
from routes.weather import weather_bp
from routes.search  import search_bp

load_dotenv()

def create_app():
    """Application factory: create & configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

   #extensions with the app
    cors.init_app(app)      #CORS forthe routes - this is to block ajax requsitions from a different origin
    cache.init_app(app)     #caching
    limiter.init_app(app)   #limiting

    # Blueprints under /api
    app.register_blueprint(weather_bp, url_prefix='/api')
    app.register_blueprint(search_bp,  url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
