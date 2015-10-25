from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from properties import *
from datetime import datetime
import smtplib

__author__ = 'Jonarzz'


def send_mails(number_of_mail_sent):
    msg = MIMEMultipart()
    msg['From'] = FROM_NAME
    msg['Subject'] = str(number_of_mail_sent) + ". " + date_now()
    msg.attach(MIMEText(str(number_of_mail_sent) + MESSAGE + date_now()))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(USERNAME, PASSWORD)

    for to_address in TO_ADDRESSES:
        server.sendmail(FROM_ADDRESS, to_address, msg.as_string())

    server.quit()


def date_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M')