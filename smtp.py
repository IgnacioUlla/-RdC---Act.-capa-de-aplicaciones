import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email():
    print("Debe ingresar un mail 'Outlook' o 'Hotmail'.")

    # Configuración
    remitente = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")
    destinatario = 'facundo.olivacuneo@unc.edu.ar'
    asunto = '[Redes de Computadoras] - Práctico SMTP.'
    cuerpo = 'Buenas tardes profesor. Este es un mail de prueba usando SMTP por parte del grupo Los BackUps.'
    
    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Agregar el cuerpo al mensaje
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Iniciar la conexión SMTP
    server = smtplib.SMTP('smtp.office365.com', 587)  # Utiliza el servidor SMTP de Outlook
    server.starttls()

    # Ingresar las credenciales
    server.login(remitente, password)

    # Enviar el correo
    text = mensaje.as_string()
    server.sendmail(remitente, destinatario, text)

    # Cerrar la conexión
    server.quit()

# Llamar a la función para enviar el correo
enviar_email()
