# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import os

account_sid = os.environ.get('ACCOUNT_SID', None)
auth_token = os.environ.get('AUTH_TOKEN', None)
application_sid = os.environ.get('APP_SID', None)

# Get these credentials from http://twilio.com/user/account
client = TwilioRestClient(account_sid, auth_token)
room_number = 0

states = ['+14158771437', '+14846794074']


def setUpCall(from_state, numbers, room):
    if len(numbers) < 2 or not 0 <= from_state < 2:
        print "error: not enough numbers for conference"
        return -1
    global client

    for num in numbers:
        call = client.calls.create(to="+1" + num,
                from_=states[from_state],
                url="http://twimlets.com/conference?Name=" +
                room + "&Message=%20")

    return call.sid


def killCall(call_id):
    call = client.calls.update(call_id, status="completed")
    print call.start_time


def cleanUpNum(num):
    num = num.translate(None, '()-')
    return num
