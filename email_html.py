import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
  # cria o servidor SMTP
  context = ssl.create_default_context()
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls(context=context)
  server.ehlo()

  # dados do remetente
  sender_email = ''
  sender_name = 'Como programar em Python'
  password = ''

  # dados do destinatário
  receivers = ['lauramattos@fundacaolemann.org.br']

  # dados do e-mail
  message = MIMEMultipart('alternative')
  message['Subject'] = 'E-mail HTML'
  message['From'] = sender_email
  message['To'] = ','.join(receivers)

  # corpo do e-mail em texto simples
  text = 'Olá :)'
  
  # corpo do e-mail em HTML
  html = 'Olá :) Clique no link para maiores informações: <a href="http://www.google.com">Google</a>'

  # atribui os dados do e-mail simples
  message.attach(MIMEText(text, 'plain'))

  # atribui os dados do e-mail HTML
  message.attach(MIMEText(html, 'html'))

  # realiza login no servidor
  server.login(sender_email, password)
  
  # envia o email
  server.sendmail(sender_email, receivers, message.as_string())

except Exception as e:
  print(f'Erros: {e}')
finally:
  # fecha o servidor
  server.quit()
