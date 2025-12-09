from email.message import EmailMessage
import smtplib

# --- Email Notification Settings ---
EMAIL_ADDRESS = "arham.bucks@gmail.com"
EMAIL_PASSWORD = "eequ cqid lhul xtdo"   # Gmail App Password


def send_email(to_email, subject, message_body):
    """Send a simple email notification using Gmail SMTP."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(message_body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def notify_customer(email, ticket_number):
    """Send a confirmation email after customer registers."""
    subject = "Queue Registration Confirmation"
    message = (
        f"Thank you for registering!\n"
        f"Your queue ticket number is: {ticket_number}\n\n"
        f"We will notify you when your number is being served."
    )

    send_email(email, subject, message)
