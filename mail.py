import os
import smtplib
from email.mime.text import MIMEText
to      = ['kime gönderilecekse',]
subject = 'PYTHON MAİL SİSTEMİ'
body    = 'Bu mesajı python ile gönderdim.'
account     = 'hesap eposta adresi'
password    = 'hesap şifresi'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(account, password)
mail = MIMEText(body, 'html', 'utf-8')
mail['From'] = account
mail['Subject'] = subject
mail['To'] = ','.join(to)
mail = mail.as_string()
try:
    server.sendmail(account, to, mail)
    print ('Mail gönderimi başarılı')
except:
    print ('Mail gönderimi başarısız')

