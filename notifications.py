from email.message import EmailMessage
import smtplib
from twilio.rest import Client

# --- Email Notification ---
EMAIL_ADDRESS = "arham.bucks@gmail.com"
EMAIL_PASSWORD = "eequ cqid lhul xtdo"  

TWILIO_SID = "AC2aea46cbad0ea35f2b4f529478a56f21"
TWILIO_AUTH_TOKEN = "aa344b490269f0b3123bfea6d57c1ea1"
TWILIO_NUMBER = "+16505388457"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_email(to_email, subject, message_body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(message_body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


# SEND SMS
def send_sms(to_phone, message_body):
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_NUMBER,
        to=to_phone
    )
    return message.sid


# COMBINED REGISTRATION NOTICE
def notify_customer(email, phone, ticket_number):
    subject = "Your Queue Registration"
    msg = f"Thank you for registering.\nYour ticket number is: {ticket_number}"

    send_email(email, subject, msg)
    send_sms(phone, msg)