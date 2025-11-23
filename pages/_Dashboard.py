# pages/_Dashboard.py
import streamlit as st
from app_state import require_login, current_user
# import navigation

st.set_page_config(page_title="Dashboard", page_icon="Home", layout="wide")

require_login()  # Redirects to login if not authenticated
# navigation.render_sidebar()

user = current_user()
st.header("Dashboard")
st.write(f"Welcome, **{user['username']}** ({user['role']})")

if user["role"] == "admin":
    st.success("Admin Panel Active")
else:
    st.info("User View")






# # Dashboard.py
# import streamlit as st
# from app_state import require_login, current_user
# import navigation

# # st.set_page_config(page_title="Dashboard")
# st.set_page_config(
#     page_title="Dashboard",
#     page_icon="🏠",
#     layout="wide"
# )


# require_login()            # Redirect to login if not authenticated
# navigation.render_sidebar()  # Sidebar menus

# user = current_user()
# st.header("🏠 Dashboard",)
# st.write(f"Welcome, **{user['username']}**")

# # Role-based content
# if user["role"] == "admin":
#     st.info("Admin features visible")
# else:
#     st.info("Standard user view")











# import streamlit as st
# from app_state import require_login, current_user, logout_user

# st.set_page_config(page_title="Dashboard")

# require_login()
# user = current_user()

# st.header("🏠 Dashboard")
# st.write(f"Welcome, **{user['username']}, {user['role']}**")

# if st.button("Logout"):
#     logout_user()

# # Example role-based view
# if user["role"] == "ADMIN":
#     st.info("Admin features")
# else:
#     st.info("Normal user view")
