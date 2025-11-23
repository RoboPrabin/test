# app_state.py
import streamlit as st

def login_user(username: str, role: str):
    st.session_state.authenticated = True
    st.session_state.username = username
    st.session_state.role = role

def is_logged_in() -> bool:
    return st.session_state.get("authenticated", False)

def require_login():
    if not is_logged_in():
        st.switch_page("_Login.py")

def current_user() -> dict:
    if not is_logged_in():
        return {"username": "", "role": ""}
    return {
        "username": st.session_state.username,
        "role": st.session_state.role
    }

def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# # app_state.py
# import streamlit as st
# from streamlit_cookies_manager import EncryptedCookieManager
# import time

# # ------ COOKIE SETUP ------
# cookies = EncryptedCookieManager(
#     prefix="trishakti_app_",  # cookie namespace
#     password="THIS_IS_SECRET_CHANGE_IT_123"  # must be constant
# )

# if not cookies.ready():
#     st.stop()


# def login_user(username, role):
#     """Sets logged in user info in encrypted cookies."""
#     cookies["logged_in"] = "1"
#     cookies["username"] = username
#     cookies["role"] = role
#     cookies.save()     # IMPORTANT


# def logout_user():
#     """Clears login cookies."""
#     cookies["logged_in"] = "0"
#     cookies["username"] = ""
#     cookies["role"] = ""
#     cookies.save()
#     st.rerun()
#     st.switch_page("_Login.py")


# def is_logged_in():
#     return cookies.get("logged_in") == "1"


# def current_user():
#     return {
#         "username": cookies.get("username"),
#         "role": cookies.get("role")
#     }


# def require_login():
#     """Redirects to login if cookie says user is not logged in."""
#     if not is_logged_in():
#         st.switch_page("_Login.py")
#         st.stop()