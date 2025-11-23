# navigation.py
import streamlit as st
from app_state import is_logged_in, current_user, logout_user

def render_sidebar():
    """
    Renders the sidebar menus based on login state and role.
    """

    lt = st.sidebar.feedback(options='faces')
    user = current_user()
    # print(str(current_user['username'].upper()))
    st.success(f"{lt}, {user['username'].upper()}")
    st.markdown("""
        <style>
            [data-testid="stSidebarCollapseButton"] {
                visibility: visible !important;
                opacity: 1 !important;
            }
        </style>
        """, unsafe_allow_html=True)
    # st.sidebar.title("Menu")
    # st.sidebar.image("https://trishakti.com.np/img/logo1.png",width=140)
    st.sidebar.markdown(
    """
    <div style='text-align:center; margin-bottom:10px;'>
        <img src='https://trishakti.com.np/img/logo1.png' width='125'>
    </div>
    <hr style='margin:30px 0 30px 0;'>
    """,
    unsafe_allow_html=True
)
    # st.sidebar.markdown("---")
    # st.sidebar.caption("-----")
    # st.markdown("<hr></hr>", unsafe_allow_html=True)

    if not is_logged_in():
        st.sidebar.page_link("_Login.py", label="Login", icon="🔐")
        return

    user = current_user()
    role = user.get("role")

    # Authenticated menus
    st.sidebar.page_link("pages/_Dashboard.py", label="Dashboard", icon="🏠")
    st.sidebar.page_link("pages/_Dashboard.py", label="Dashboard", icon="🏠")
    st.sidebar.page_link("pages/_Dashboard.py", label="Dashboard", icon="🏠")
    st.sidebar.page_link("pages/_Dashboard.py", label="Dashboard", icon="🏠")
    st.sidebar.page_link("pages/_Dashboard.py", label="Dashboard", icon="🏠")

    # if role == "bro":
    #     st.sidebar.page_link("4_🧑‍🦱_Bro Limit", label="BRO Summary")
    # if role == "manager":
    #     st.sidebar.page_link("5_👨‍💼_Manager Summary", label="Manager Summary")
    # if role == "admin":
    #     st.sidebar.page_link("6_➕_Create App User", label="Admin Panel")

    # Logout
    if st.sidebar.button("Logout"):
        logout_user()
        st.switch_page("_Login")
    
    with st.sidebar:
    # ... your other sidebar items ...

        st.markdown("""<div style="margin-top: 160px;"></div>""", unsafe_allow_html=True)  # spacer
        st.markdown(
            "<p style='text-align: center; color: gray; font-size: 12px;'>"
            "© Trishakti Securities Limited.<br>All Rights Reserved."
            "</p>",
            unsafe_allow_html=True
        )