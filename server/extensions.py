from flask_cors import CORS
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize extensions (no app yet)
cors   = CORS()
cache  = Cache()
limiter = Limiter(key_func=get_remote_address)
