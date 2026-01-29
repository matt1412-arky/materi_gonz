from flask import Flask, render_template, request

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

if __name__ == '__main__':
    app.run(debug=True)
