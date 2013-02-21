from twilio.rest import TwilioRestClient

account_sid = "AC566da319c49345fe4fbbbea81ada1de0"
auth_token = "741080b04bcb6c2471cf9439d939abce"

client = TwilioRestClient(account_sid, auth_token)
queues = client.queues.list()

for queue in queues:
	print queue.sid
