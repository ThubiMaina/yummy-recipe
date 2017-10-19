import os
from app import app
# Enable Flask's debugging features.
DEBUG = True
app.secret_key = os.urandom(24)