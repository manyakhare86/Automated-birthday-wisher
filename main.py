##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime as dt
import smtplib

email_id = "mkhare8610@gmail.com"
password = "ot*********od"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
df = pandas.read_csv("birthdays.csv")
print(df)
data = df.to_dict(orient="records")
print(data)
now = dt.datetime.now()
day = now.day
month = now.month
year = now.year

for detail in data:
    print(detail)
    if detail['day'] == day and detail['month'] == month:
        name = detail['name']
    with open(f"letter_templates\letter_{random.randint(1,3)}.txt") as letter:
        msg = letter.read()
        named_msg = msg.replace("[NAME]", f"{name}")

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_id, password=password)
        connection.sendmail(from_addr=email_id, to_addrs=detail['email'],
                            msg=f"Subject:Happy Birthday!\n\n {named_msg}")