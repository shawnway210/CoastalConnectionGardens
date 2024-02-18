import secrets

SECRET_KEY = secrets.token_hex(16)
JWT_SECRET_KEY = secrets.token_hex(16)