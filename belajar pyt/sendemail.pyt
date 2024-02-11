# namaSayaik@n99
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Informasi akun email Anda
email_pengirim = 'appsecurty@gmail.com'
password = 'Securty1910'

# Informasi penerima email
email_penerima = 'zaldyramlan24@gmail.com'

# Membuat pesan email
subjek = 'Ini adalah subjek email'
pesan = 'Ini adalah isi pesan email.'

msg = MIMEMultipart()
msg['From'] = 'appssecurty@gmail.com'
msg['To'] = email_penerima
msg['Subject'] = subjek

msg.attach(MIMEText(pesan, 'plain'))

# Mengirim email menggunakan SMTP
try:
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('appsecurty@gmail.com', 'Securty1910')
    server.sendmail(email_pengirim, email_penerima, msg.as_string())
    print('Email berhasil dikirim!')
except Exception as e:
    print('Email gagal dikirim:', str(e))
