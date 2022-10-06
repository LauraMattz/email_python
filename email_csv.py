import csv
import smtplib
import ssl

try:
  # cria o servidor SMTP
  context = ssl.create_default_context()
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls(context=context)
  server.ehlo()

  # dados do remetente
  sender_email = ''
  sender_name = 'Como Programar em Python'
  password = ''
  subject = 'E-mail personalizado'

  # realiza login no servidor
  server.login(sender_email, password)

  # percorre a lista de alunos
  # enviando e-mails personalizados
  # para cada um deles com a respectiva nota
  for aluno in csv.DictReader(open(r'C:\Users\lmattos\alunos.csv')):
    nome = aluno['nome']
    email = aluno['email']
    nota = aluno['nota']

    # dados do e-mail
    body = f'Ola {nome}, sua nota foi {nota}.'
    receivers = [email]
    message = f'From:{sender_name}\nSubject:{subject}\n\n{body}'

    # envia o e-mail personalizado
    server.sendmail(sender_email, receivers, message)

except Exception as e:
  print(f'Erros: {e}')
finally:
  # fecha o servidor
  server.quit()
