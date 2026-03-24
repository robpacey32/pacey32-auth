# shared/auth_db.py
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone

MONGO_URI = "..."  # Can be passed in via secrets/env vars

client = MongoClient(MONGO_URI)
db = client["auth_db"]

users_col = db["users"]
sessions_col = db["sessions"]

def create_user_session(username, days=30):
    token = generate_random_token()
    expires_at = datetime.now(timezone.utc) + timedelta(days=days)
    sessions_col.insert_one({
        "username": username,
        "token": token,
        "expires_at": expires_at
    })
    return token

def get_user_session_by_token(token):
    return sessions_col.find_one({"token": token})
    
# And so on for delete_user_session_by_token, extend_user_session, get_user_by_username, etc.