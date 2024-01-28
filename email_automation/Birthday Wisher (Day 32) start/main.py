import smtplib

my_email = "kumarnotnice2@gmail.com"
password = "diSpyf-zyxzaj-6dyjjo"
connection = smtplib.SMTP("smtp.gamil.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Hello abhishek")
connection.close()


