from email.message import EmailMessage
import smtplib

EMAIL_ADDRESS = "arham.bucks@gmail.com"
EMAIL_PASSWORD = "eequ cqid lhul xtdo"

msg = EmailMessage()
msg["Subject"] = "Queue System Test"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "arhamkalam321@gmail.com"
msg.set_content("Your queue system email is working!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Email sent!")
