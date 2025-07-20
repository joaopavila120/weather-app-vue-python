import os
from dotenv import load_dotenv

# Load .env into environment
load_dotenv()

class Config:
    # OpenWeatherMap API key
    OPENWEATHER_KEY = os.getenv('OPENWEATHER_KEY')
    if not OPENWEATHER_KEY:
        raise RuntimeError('OPENWEATHER_KEY env var is not set.')

    #caching configuration
    CACHE_TYPE = 'SimpleCache' # in-memory cache
    CACHE_DEFAULT_TIMEOUT = 600 # default TTL = 600s -10 min)

    #rate limiting configuration
    RATELIMIT_DEFAULT = '100 per hour'   
    RATELIMIT_HEADERS_ENABLED = True    
