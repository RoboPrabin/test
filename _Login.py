# Login.py
import streamlit as st
from utils.db import get_user_by_username
from app_state import login_user, is_logged_in

st.set_page_config(page_title="Login", layout="centered")

if is_logged_in():
    st.switch_page("pages/_Dashboard.py")

st.title("Login")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        user = get_user_by_username(username)
        if user and password == user["password"]:
            login_user(user["username"], user["role"])
            st.success("Login successful!")
            st.rerun()  # This instantly redirects
        else:
            st.error("Invalid credentials")





# # Login.py
# import streamlit as st
# from utils.db import get_user_by_username
# from app_state import login_user, is_logged_in
# import navigation
# import time

# st.set_page_config(page_title="Login", layout="centered")

# #  If already logged in, redirect automatically
# if is_logged_in():
#     st.success("Already logged in, redirecting...")
#     time.sleep(0.5)
#     st.switch_page("pages/_Dashboard.py")

# #  navigation.render_sidebar()   Optional: show sidebar even on login

# st.title("🔐 Login")

# with st.form("login_form"):
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     submitted = st.form_submit_button("Login")

# if submitted:
#     user = get_user_by_username(username)
#     if user and password == user["password"]:
#         login_user(user["username"], user["role"])
#         st.success("Login successful! Redirecting...")
#         time.sleep(0.5)
#         st.switch_page("pages/_Dashboard.py")
#     else:
#         st.error("Invalid username or password.")











#  import streamlit as st
#  from utils.db import get_user_by_username
#  from app_state import login_user, is_logged_in
#  import time

#  st.set_page_config(page_title="Login", layout="centered")

#   If already logged in, redirect automatically
#  if is_logged_in():
#      st.success("Already logged in, redirecting...")
#      time.sleep(0.5)
#      st.switch_page("pages/2_🏠_Dashboard.py")

#  st.title("🔐 Login")

#  with st.form("login_form"):
#      username = st.text_input("Username")
#      password = st.text_input("Password", type="password")
#      submitted = st.form_submit_button("Login")

#  if submitted:
#      user = get_user_by_username(username)

#      if user is None:
#          st.error("Invalid username or password.")
#      else:
#          if password == user["password"]:
#              login_user(user["username"], user["role"])
#              st.success("Login successful! Redirecting...")
#              time.sleep(0.5)
#              st.switch_page("pages/2_🏠_Dashboard.py")
#          else:
#              st.error("Invalid username or password.")
