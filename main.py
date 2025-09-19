
from twilio.rest import Client

account_sid = 'AC6712ce5c48f555eeb9f3fa074bb0fa84'
auth_token = '8c855121f4cdf1ff643a817c1661ba1f'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18559451964',
  body='What made you smile today?',
  to='+18001231234'
)

print(message.sid)
