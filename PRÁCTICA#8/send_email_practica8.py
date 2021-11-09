#!/usr/bin/env python3
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import argparse
import requests 

if __name__ == "__main__":
  description="Este script tiene la finalidad de mandar correos electronicos"
  parser = argparse.ArgumentParser(description="Practica 8", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-usuario', type=str , help='Correo de envío.')
  parser.add_argument('-receptor', type=str , help='Correo de recepción.')
  parser.add_argument('-url', type=str , help='Pagina web.')
  parser.add_argument('-contra', type=str , help='Contraseña.')
  parser.add_argument('-msj', type=str,default = "Saludos.")
  parser.add_argument('-asunto', type=str, default="Hola.")
  params = parser.parse_args()


url = (params.url)
usuario = (params.usuario)
receptor = (params.receptor)
mensaje = (params.msj)
asunto = (params.asunto)
contraseña = (params.contra)

email_msg = MIMEMultipart("alternative")
email_msg["From"] = usuario
email_msg["To"] = receptor
email_msg["Subject"] = asunto

email_msg.attach(MIMEText(mensaje, "plain"))

pag = requests.get(url)
soup = bs(pagina.content,"html.parser")

archivo = "arch.txt"
arch = open(arch, "a")
contenido = soup.find_all("p")[:3]
for p in cont:
    cont = p.get_text()
    arch.write(cont)
arch.close()


filename = arch  
with open(filename, "rb") as attachment:
    
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
 

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",)


email_msg.attach(part)


context = ssl.create_default_context()
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(usuario, contra)
    server.sendmail(
        usuario, receptor, email_msg.as_string()
    )
print("correo enviado correctamente: %s" % (receptor))
