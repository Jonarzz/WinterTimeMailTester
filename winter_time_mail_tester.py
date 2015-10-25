from server_configurator import send_mails
from datetime import datetime
from properties import SEND_DATES
import time

__author__ = 'Jonarzz'


print("START")
dates_to_send_on = SEND_DATES
i = 0
while True:
    if datetime.now().strftime('%Y-%m-%d %H:%M') in dates_to_send_on:
        dates_to_send_on.remove(datetime.now().strftime('%Y-%m-%d %H:%M'))
        i += 1
        send_mails(i)
        print("Sent mail number " + str(i))
    if not dates_to_send_on:
        print(str(i) + " mails sent.")
        break
    time.sleep(30)
