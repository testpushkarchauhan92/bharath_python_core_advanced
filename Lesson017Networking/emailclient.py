import smtplib
from email.mime.text import MIMEText

body = "This is a test email from Python Program emailclient.py .How are you?"

msg = MIMEText(body)
msg['From'] = "pctestingacc@gmail.com"
msg['To'] = "pctestingacc@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("pctestingacc@gmail.com","Appl31ph0n3")

server.send_message(msg)

print("Mail sent")

server.quit()
