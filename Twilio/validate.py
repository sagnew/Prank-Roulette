from twilio.rest import TwilioRestClient

account_sid = "AC566da319c49345fe4fbbbea81ada1de0"
auth_token = "741080b04bcb6c2471cf9439d939abce"

client = TwilioRestClient(account_sid, auth_token)
response = client.caller_ids.validate("+1 4846844944")
print response.validation_code
