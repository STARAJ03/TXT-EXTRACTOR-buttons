import os
from os import getenv

API_ID = int(os.environ.get("27765349", ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("9df1f705c8047ac0d723b29069a1332b", "")
BOT_TOKEN = os.environ.get("", "")

OWNER_ID = int(os.environ.get("1116405290", ""))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("1116405290", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("mongodb+srv://allclashwithaj:<iamagamer>@cluster0.xmdob.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("-1001116405290", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("1116405290", "")  # Optional here you'll get all logs
