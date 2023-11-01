import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Define your email settings
sender_email = 'mr.venci27@gmail.com'
sender_password = 'patp rlcw oles djet'
recipient_email = 'radodimitrov93@gmail.com'


today = datetime.now()
birthday = datetime(today.year, 11, 15)
days_until_birthday = (birthday - today).days

# Create the email message
subject = 'Предстоящ upgrade от Дърво 2.9 към г-н Дърво 3.0'
message = f'Добър ден,\n\nЖелаем да ви уведомим за предстоящ update след  {days_until_birthday} дни.\n Ъпдейта е задължителен и неизбежен!\n Честито! 🎉\n\nЖив и здрав де,\nОт бате Венци и кака Марла'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print('Email sent successfully.')
except Exception as e:
    print(f'Email could not be sent. Error: {str(e)}')
