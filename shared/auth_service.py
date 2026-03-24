# shared/auth_service.py
from datetime import datetime, timezone
import bcrypt
from shared.auth_db import (
    users_col,
    update_last_login,
    update_user_password,
    delete_all_user_sessions,
    create_email_verification_token,
    create_password_reset_token,
    get_user_by_email,
    mark_user_email_verified,
    get_email_verification_by_token,
    delete_email_verification_by_token,
    get_password_reset_by_token,
    delete_password_reset_by_token,
)

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

# rest of login/register/reset functions here