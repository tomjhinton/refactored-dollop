import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/refactored-dollop')
secret = os.getenv('SECRET', 'a suitable secret')
