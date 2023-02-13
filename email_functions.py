import os
import smtplib, ssl
import pdf_creator


def create_email_content(message):
    print("CREATING EMAIL")
    

    pdf_creator.create_pdf(message)
    # TODO send over to create pdf functions

    # TODO send back to the send_email OOP function-- which will then call the send_email function


def send_email(message, address):
    # print("SENDDD")
    # print(message)
    # print(address)
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