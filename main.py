import pandas as pd
import random
import smtplib
import datetime as dt

today_date=dt.datetime.now().day
today_month=dt.datetime.now().month

my_email="aj0040976@gmail.com"
password="uvqyhozbxiumjibq"

dataframe=pd.read_csv("birthdays.csv")
found=dataframe[(dataframe["day"]==today_date) & (dataframe["month"]==today_month)]
found_list=found.values.tolist()

list_length=len(found_list)

if list_length>0:
    for i in found_list:
        number=random.randint(1,3)

        file=open(f"./letter_templates/letter_{number}.txt","r")
        content=file.read()
        new_content=content.replace("[NAME]",i[0])
        file.close()

        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=i[1],msg=f"subject:Birthday Greeting\n\n{new_content}")
        connection.close()













