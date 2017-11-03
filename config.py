import os
from app import app
# Enable Flask's debugging features.
DEBUG = True
PORT = 5000
app.secret_key = os.urandom(24)