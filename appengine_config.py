def webapp_add_wsgi_middleware(app):
    from engineauth import middleware
    return middleware.AuthMiddleware(app)

from secret_keys import CSRF_SECRET_KEY, SESSION_KEY

engineauth = {
    'secret_key': CSRF_SECRET_KEY,
    'user_model': 'engineauth.models.User',
}

engineauth['provider.auth'] = {
    'user_model': 'engineauth.models.User',
    'session_backend': 'datastore',
}

# Facebook Authentication
engineauth['provider.facebook'] = {
    'client_id': 'CHANGE_TO_FACEBOOK_APP_ID',
    'client_secret': 'CHANGE_TO_FACEBOOK_CLIENT_SECRET',
    'scope': 'email',
}

# Google Plus Authentication
engineauth['provider.google'] = {
    'client_id': 'CHANGE_TO_GOOGLE_CLIENT_ID',
    'client_secret': 'CHANGE_TO_GOOGLE_CLIENT_SECRET',
    'api_key': 'CHANGE_TO_GOOGLE_API_KEY',
    'scope': 'https://www.googleapis.com/auth/plus.me',
}

# Twitter Authentication
engineauth['provider.twitter'] = {
    'client_id': 'CHAGNE_TO_TWITTER_CONSUMER_KEY',
    'client_secret': 'CHAGNE_TO_TWITTER_CONSUMER_SECRET',
}
