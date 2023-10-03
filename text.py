from twilio.rest import Client
import os

account_sid = 'ACed03ce8e3c901a1466942d8838b126d9'
auth_token = '70ee634e38245e7cc7669593f40468b6'

client = Client(account_sid, auth_token)


message = client.messages \
    .create(
        body='Hello there from Twilio SMS API',
        from_=+15734002105,
        to=+918129431033
    )

print(message.sid)
