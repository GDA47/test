import streamlit as st
import pandas as pd

st.set_page_config(page_title="Login", page_icon="🔒", layout="centered")

# --- Load credentials ---
def load_users():
    df = pd.read_excel("users.xlsx")
    df['username'] = df['username'].astype(str)
    df['password'] = df['password'].astype(str)
    return df

# --- UI ---
st.image("logo.png", width=200)  # Optional logo
st.title("🔒 Secure Login")

username = st.text_input("👤 Username")
password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    users = load_users()

    # Check credentials
    if ((users['username'] == username) & (users['password'] == password)).any():
        st.session_state["authenticated"] = True
        st.session_state["user"] = username
        st.success("✅ Login successful!")
        st.switch_page("pages/dashboard.py")
    else:
        st.error("❌ Invalid username or password")
