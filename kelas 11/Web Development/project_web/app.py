from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def passing_data():
   # Data yang akan dikirim ke template
    nama = "Ali Rahman"
    kelas = "XI RPL"
    hobi = ["Coding", "Gaming", "Membaca"]
    
    return render_template('home.html', 
                         nama=nama, 
                         kelas=kelas, 
                         hobi=hobi)
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Mengambil data dari form
    nama = request.form.get('nama')
    kelas = request.form.get('kelas')
    email = request.form.get('email')
    hobi = request.form.get('hobi')
    
    # Kirim ke template hasil
    return render_template('hasil.html',
                         nama=nama,
                         kelas=kelas,
                         email=email,
                         hobi=hobi)
# Fungsi untuk koneksi database
def get_db():
    conn = sqlite3.connect('C:/Users/Lenovo/OneDrive/Documents/materi_gonz/kelas 11/Web Development/project_web/static/db/siswa.db')
    conn.row_factory = sqlite3.Row
    return conn

# Membuat tabel
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        kelas TEXT NOT NULL,
        email TEXT,
        hobi TEXT
    )
    """)
    conn.commit()
    conn.close()

# Route halaman utama - tampilkan semua siswa
@app.route('/database')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM siswa ORDER BY nama")
    siswa = cursor.fetchall()
    conn.close()
    
    return render_template('index_db.html', siswa=siswa)

# Route form tambah siswa
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        kelas = request.form['kelas']
        email = request.form['email']
        hobi = request.form['hobi']
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO siswa (nama, kelas, email, hobi)
        VALUES (?, ?, ?, ?)
        """, (nama, kelas, email, hobi))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('form_tambah.html')

# Route hapus siswa
@app.route('/hapus/<int:id>')
def hapus(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM siswa WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Buat tabel jika belum ada
    app.run(debug=True)
