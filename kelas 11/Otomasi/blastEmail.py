import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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

# Cara pakai
if __name__ == "__main__":
    sender = "matthew.christian@gonzaga.sch.id"
    password = "aigm lulb hogh wvmu"  # Gunakan App Password, bukan password biasa!
    recipient = "38.jose.madur@gonzaga.sch.id"
    
    subject = "Materi Hari Ini"
    body = """
    Hai Jose,
    
    Terlampir adalah Materi Hari ini.
    
    Terima kasih!
    """
    
    attachment = r"C:\Users\Lenovo\OneDrive\Documents\materi_gonz\kelas 11\Otomasi\Otomasi.pdf"
    
    send_email(sender, password, recipient, subject, body, attachment)




