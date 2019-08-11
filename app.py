from twilio.rest import Client
import config

sid = config.account_sid
token = config.auth_token

client = Client(sid, token)


call = client.messages.create(
    to="phone_no",
    from_="twilio_registered_no",
    body="Your Message"
)
