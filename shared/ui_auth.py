# shared/ui_auth.py
import streamlit as st
from streamlit_local_storage import LocalStorage
from shared.auth_service import login_user, register_user, request_password_reset
from shared.auth_db import (
    create_user_session,
    get_user_session_by_token,
    delete_user_session_by_token,
    extend_user_session,
    get_user_by_username,
)
from shared.email_utils import send_verification_email, send_password_reset_email
from shared.styles import apply_umbreon_theme

# SESSION CONSTANTS
SESSION_DAYS = 30
SESSION_STORAGE_KEY = "session_token"

# All the Streamlit UI logic you currently have:
# restore_login_from_storage(), save_session_to_storage(), clear_session_from_storage(), logout(), render_login_portal()
# Only change imports to reference shared.auth_service and shared.auth_db