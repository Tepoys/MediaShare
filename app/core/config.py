# Tepoys
# core/config.py
# Configuration and data storage

import os

JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_ALGORITHM = "HS256"
