import os
import smtplib, ssl


def create_email_content(message):
    print("CREATING EMAIL")
    print(message)

def send_email(message, address):
    host = 'smtp.gmail.com'
    port = 465

    # ! Change this to a regular account
    # ! Temp
    username = 'bjsmerd@gmail.com'
    password = os.getenv('PASSWORD')

    # ? receiver will be the address sent in, mine for temp
    receiver = 'bjsmerd@gmail.com'
    # receiver = address
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)