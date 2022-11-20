import smtplib
import pandas
import datetime as dt


my_email = ""
password = ""


name_placeholder = "[NAME]"



# find whose birthday
now = dt.datetime.now()
day = now.day
month = now.month
b_d = (month, day)

# get the csv in a ready format
birthday_df = pandas.read_csv("birthdays.csv")
birthdays = {(row.month, row.day, row.name): [row.b_name, row.email] for (index, row) in birthday_df.iterrows()}
birth_dates = [birth_date[:-1] for birth_date in birthdays.keys()]


# send mail
if b_d in birth_dates:

    for i in range(19):
        if (month, day, i) in birthdays:
            # get name
            name = birthdays[(month,day,i)][0]
            to_mail = birthdays[(month,day,i)][1]

            # prepare the letter
            with open("letter.txt") as letter:
                contents = letter.read()
                contents = contents.replace(name_placeholder, name)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email , password=password)
                connection.sendmail(from_addr=my_email,
                to_addrs=to_mail,
                msg=f"Subject:Happy Birthday!\nTo:{my_email}\n{contents}")






