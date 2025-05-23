# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Dummy login
USER_CREDENTIALS = {"admin": "admin123"}

# Session state untuk login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.success("Login berhasil!")
        else:
            st.error("Username/password salah")

def logout():
    st.session_state.logged_in = False

def main():
    st.sidebar.title("Navigasi")
    model = st.sidebar.selectbox("Pilih Model", ["TimeGPT", "ARIMA", "SARIMA"])
    st.sidebar.button("Logout", on_click=logout)

    st.title(f"Hasil Forecasting - {model}")

    uploaded_file = st.file_uploader("Upload file hasil forecasting (.csv)", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Data Forecasting:")
        st.dataframe(df)

        # Plot jika ada kolom 'actual' dan 'forecast'
        if 'actual' in df.columns and 'forecast' in df.columns:
            fig = px.line(df, x='date', y=['actual', 'forecast'], title=f"Plot Forecast {model}")
            st.plotly_chart(fig)

if __name__ == "__main__":
    if st.session_state.logged_in:
        main()
    else:
        login()
