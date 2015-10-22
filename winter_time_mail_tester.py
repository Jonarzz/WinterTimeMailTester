from server_configurator import send_mails
from datetime import datetime
from properties import SEND_DATES

__author__ = 'Jonarzz'


dates_to_send_on = SEND_DATES
i = 0
while True:
    i += 1
    if datetime.now().strftime('%Y-%m-%d %H:%M') in dates_to_send_on:
        dates_to_send_on.remove(datetime.now().strftime('%Y-%m-%d %H:%M'))
        send_mails(i)
    if not dates_to_send_on:
        break
