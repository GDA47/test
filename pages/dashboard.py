import streamlit as st

# --- Authentication check ---
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔒 You must log in first.")
    st.stop()

# --- Main content ---
st.title("📊 Welcome to the Dashboard")
st.write(f"Hello, **{st.session_state['user']}** 👋")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
