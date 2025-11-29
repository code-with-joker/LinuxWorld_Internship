from twilio.rest import Client

ACCOUNT_SID = "xxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxx"
TWILIO_NUMBER = "+12034567890"

RECIVER_NUMBER = "+1234567890"

client = Client(ACCOUNT_SID,AUTH_TOKEN)
msg = client.messages.create(
    body= "Hello I am Kishan Kumar",
    from_= TWILIO_NUMBER,
    to=RECIVER_NUMBER                            
)
print(msg.sid)