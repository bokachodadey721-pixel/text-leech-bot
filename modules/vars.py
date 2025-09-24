import os

API_ID    = os.environ.get("API_ID", "16818865")
API_HASH  = os.environ.get("API_HASH", "2855f44c4724e69a86885f14de875a21")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
