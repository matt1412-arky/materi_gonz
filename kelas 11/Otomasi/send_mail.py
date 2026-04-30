import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import time

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        if attachment:
            with open(attachment, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {attachment}')
                msg.attach(part)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"✅ Email berhasil dikirim ke {recipient_email}")
        return True
        
    except Exception as e:
        print(f"❌ Error mengirim ke {recipient_email}: {e}")
        return False


def send_bulk_emails(sender_email, sender_password, csv_file):
    df = pd.read_csv(csv_file)
    
    print(f"📧 Akan mengirim email ke {len(df)} penerima\n")
    
    success = 0
    failed = 0
    
    for index, row in df.iterrows():
        nama     = row['nama']
        email    = row['email']
        password = row['password']
        
        subject = f"Informasi Akun - {nama}"
        body = f"""Halo {nama},

Berikut adalah informasi akun kamu:

Email    : {email}
Password : {password}

Segera ganti password kamu setelah login pertama kali.

Salam,
Pak Matthew
"""
        
        print(f"📤 Mengirim ke {nama} ({email})...")
        
        if send_email(sender_email, sender_password, email, subject, body):
            success += 1
        else:
            failed += 1
        
        time.sleep(2)
    
    print(f"\n📊 Statistik:")
    print(f"✅ Berhasil: {success}")
    print(f"❌ Gagal: {failed}")


if __name__ == "__main__":
    sender   = "matthew.christian@gonzaga.sch.id"
    password = "zhov ittk ckep taxk"
    csv_file = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\Otomasi\daftar_akun.csv"

    send_bulk_emails(sender, password, csv_file)