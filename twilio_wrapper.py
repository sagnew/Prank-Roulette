# Download the library from twilio.com/docs/libraries
from twilio.rest import Client
import os

account_sid = os.environ.get('ACCOUNT_SID', None)
auth_token = os.environ.get('AUTH_TOKEN', None)
application_sid = os.environ.get('APP_SID', None)

# Get these credentials from http://twilio.com/user/account
client = Client(account_sid, auth_token)
room_number = 0

# Your Twilio phone number
twilio_number = os.environ.get('TWILIO_PHONE_NUMBER', None)


def setUpCall(from_state, numbers, room):
    if len(numbers) < 2:
        print("error: not enough numbers for conference")
        return -1
    global client
    global twilio_number

    # Call both people using your Twilio number as caller ID
    call1 = client.calls.create(
        to="+1" + numbers[0],
        from_=twilio_number,
        url="http://twimlets.com/conference?Name=" + room + "&Message=%20"
    )
    
    call2 = client.calls.create(
        to="+1" + numbers[1],
        from_=twilio_number,
        url="http://twimlets.com/conference?Name=" + room + "&Message=%20"
    )

    return call2.sid


def killCall(call_id):
    call = client.calls(call_id).update(status="completed")
    print(call.start_time)


def cleanUpNum(num):
    num = num.translate(str.maketrans('', '', '()-'))
    return num
