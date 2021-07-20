import smtplib

s = smtplib.SMTP("smtp.gmail.com", 587)
sender_email_id = "retshepilekoloko27@gmail.com"
receiver_email_id = "likhokapesi135@gmail.com", "mndabeni6@gmail.com"
password = input("Enter sender password:")


s.starttls()

s.login(sender_email_id, password)

message = "Hi, hope you well. I'm still not fine"
message = message + "Andisagowi"

s.sendmail(sender_email_id, receiver_email_id, message)

s.quit()
