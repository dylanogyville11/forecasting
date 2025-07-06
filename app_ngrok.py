from pyngrok import ngrok
import streamlit.web.cli as stcli
import sys

# Mulai ngrok tunnel di port 8501 (port default Streamlit)
public_url = ngrok.connect(port=8501)
print("Aplikasi tersedia di:", public_url)

# Jalankan Streamlit
sys.argv = ["streamlit", "run", "app.py"]  # ganti dengan nama file kamu
stcli.main()

print("🚀 Memulai Streamlit + Ngrok...")
