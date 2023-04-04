import os
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from _4_11_template import dados
from dotenv import load_dotenv

CAMINHO_ARQ = Path(__file__).parent / "email_template.html"

load_dotenv()

# print(os.environ)
remetente = os.getenv('EMAIL', '')
destinatario = remetente
smtp_email = 'smtp.gmail.com'
smtp_port = 587
user = remetente
password = os.getenv('EMAIL_PASSWORD', '')


with open(CAMINHO_ARQ, 'r') as arq:
    texto = arq.read()
    template = string.Template(texto)
    texto_envio = template.substitute(dados)

print(texto_envio)

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'O assunto do e-mail'
#  ! Caso use texto puro subtype = plain
corpo_email = MIMEText(texto_envio, 'html', 'UTF-8')
mime_multipart.attach(corpo_email)


with smtplib.SMTP(smtp_email, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso')
