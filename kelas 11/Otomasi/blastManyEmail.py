import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import time

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment=None):
    """
    Kirim email dengan atau tanpa attachment
    """
    
    try:
        # Setup email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Body email
        msg.attach(MIMEText(body, 'plain'))
        
        # Attachment (jika ada)
        if attachment:
            with open(attachment, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {attachment}')
                msg.attach(part)
        
        # Koneksi ke Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Kirim email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"✅ Email berhasil dikirim ke {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
def send_bulk_emails(sender_email, sender_password, csv_file):
    """
    Kirim email ke banyak penerima dari file CSV
    
    CSV format:
    nama,email,nilai
    Ali,ali@email.com,85
    Budi,budi@email.com,90
    """
    
    # Baca data dari CSV
    df = pd.read_csv(csv_file)
    
    print(f"📧 Akan mengirim email ke {len(df)} penerima\n")
    
    success = 0
    failed = 0
    
    for index, row in df.iterrows():
        nama = row['nama']
        email = row['email']
        nilai = row['nilai']
        
        # Personalisasi subject dan body
        subject = f"Nilai Ujian - {nama}"
        body = f"""
        Halo {nama},
        
        Berikut adalah nilai ujian kamu:
        Nilai: {nilai}
        
        {"Selamat! Nilai kamu bagus!" if nilai >= 75 else "Tetap semangat! Belajar lebih giat lagi."}
        
        Salam,
        Guru
        """
        
        print(f"📤 Mengirim ke {nama} ({email})...")
        
        if send_email(sender_email, sender_password, email, subject, body):
            success += 1
        else:
            failed += 1
        
        # Jeda agar tidak dianggap spam
        time.sleep(2)
    
    print(f"\n📊 Statistik:")
    print(f"✅ Berhasil: {success}")
    print(f"❌ Gagal: {failed}")

# Cara pakai
if __name__ == "__main__":
    sender = "matthew.christian@gonzaga.sch.id"
    password = "zhov ittk ckep taxk"
    csv_file = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\Otomasi\daftar_nilai.csv"
    
    send_bulk_emails(sender, password, csv_file)
