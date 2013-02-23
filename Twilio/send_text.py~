# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "AC566da319c49345fe4fbbbea81ada1de0"
auth_token = "741080b04bcb6c2471cf9439d939abce"
client = TwilioRestClient(account_sid, auth_token)

# send text
message = client.sms.messages.create(to="+19065287844",
		from_="+14159686840",
		body="freakin twilio man")

print message.sid
