import streamlit as st
import pandas as pd
import plotly.express as px
import time
import os

# Dummy login
USER_CREDENTIALS = {"admin": "admin123"}

# Inisialisasi session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'forecast_data' not in st.session_state:
    st.session_state.forecast_data = None

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.success("Login berhasil!")
            time.sleep(1)
            st.rerun() # <-- Ganti di sini juga
        else:
            st.error("Username/password salah")

def logout():
    st.session_state.logged_in = False
    st.success("Berhasil logout!")
    time.sleep(1)
    st.rerun() # <-- Ganti di sini

def main():
    # --- KUMPULKAN SEMUA ELEMEN SIDEBAR DI SINI ---
    st.sidebar.title("Navigasi")
    model = st.sidebar.selectbox("Pilih Model Forecast", ["Forecast_ARIMA", "Forecast_TimeGPT", "Forecast_SARIMAX"])
    st.sidebar.button("Logout", on_click=logout)
    # ----------------------------------------------

    st.title("Hasil Forecasting Saham")
    # `selectbox` sudah tidak ada di sini lagi

    if st.session_state.forecast_data is None:
        if os.path.exists("forecast_stocksastra_target - grafik.csv"):
            df = pd.read_csv("forecast_stocksastra_target - grafik.csv")
            st.session_state.forecast_data = df
        else:
            st.warning("File 'forecast_stocksastra_target - grafik.csv' tidak ditemukan.")
            return

    df = st.session_state.forecast_data

    st.subheader("Data Forecasting")
    st.dataframe(df)

    actual_col = "actual  value"

    if 'date' in df.columns and actual_col in df.columns and model in df.columns:
        fig = px.line(df, x='date', y=[actual_col, model],
                      labels={'value': 'Harga', 'date': 'Tanggal'},
                      title=f"Perbandingan Actual dan {model}")
        st.plotly_chart(fig)
    else:
        st.warning("Data tidak memiliki kolom yang dibutuhkan untuk grafik.")

if __name__ == "__main__":
    if st.session_state.logged_in:
        main()
    else:
        login()
