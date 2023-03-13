from random import choice

import smtplib
import pandas as pd
import datetime as dt

sender = "@gmail.com"
passcode = ""

birthdays = pd.read_csv("birthdays.csv")
birthdays = birthdays.to_dict(orient='records')

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

for bd in birthdays:

    if int(bd["month"]) == today_month and today_day == int(bd["day"]):

        with open(f"./letter_templates/letter_{choice([1, 2, 3])}.txt") as template:
            template_text = template.read()
            letter_content = template_text.replace("[NAME]", bd["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender, password=passcode)
            connection.sendmail(
                from_addr=sender,
                to_addrs=bd["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_content}"
            )
