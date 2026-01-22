# app.py
from flask import Flask

# Membuat aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    return "<h1>Hello World!</h1><p>Website pertamaku dengan Flask 🚀</p>"

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
