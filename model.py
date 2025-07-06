import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Judul aplikasi
st.title("Hasil Forecasting Saham")

# Sidebar untuk memilih model
st.sidebar.title("Navigasi")
model = st.sidebar.selectbox("Pilih Model Forecast", ["Forecast_ARIMA", "Forecast_TimeGPT", "Forecast_SARIMAX"])

# Load data jika belum dimuat
if 'forecast_data' not in st.session_state:
    if os.path.exists("forecast_stocksastra_target - grafik.csv"):
        df = pd.read_csv("forecast_stocksastra_target - grafik.csv")
        st.session_state.forecast_data = df
    else:
        st.warning("File 'forecast_stocksastra_target - grafik.csv' tidak ditemukan.")
        st.stop()

df = st.session_state.forecast_data

# Tampilkan tabel
st.subheader("Data Forecasting")
st.dataframe(df)

# Visualisasi
actual_col = "actual  value"  # Sesuaikan jika perlu (perhatikan spasi)

if 'date' in df.columns and actual_col in df.columns and model in df.columns:
    fig = px.line(df, x='date', y=[actual_col, model],
                  labels={'value': 'Harga', 'date': 'Tanggal'},
                  title=f"Perbandingan Actual dan {model}")
    st.plotly_chart(fig)
else:
    st.warning("Data tidak memiliki kolom yang dibutuhkan untuk grafik.")
