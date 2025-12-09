from twilio.rest import Client

sid = "AC2aea46cbad0ea35f2b4f529478a56f21"
auth = "aa344b490269f0b3123bfea6d57c1ea1"
client = Client(sid, auth)

message = client.messages.create(
    body="Test message from Twilio.",
    from_="+16505388457",
    to="+447435646700"  # Your verified number
)

print(message.sid)




