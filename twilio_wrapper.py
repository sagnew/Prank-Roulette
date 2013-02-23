# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from twilio import twiml
from string import translate
import random


# Get these credentials from http://twilio.com/user/account
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)
room_number = 0;

states = ['+14846854944', '+14159686840']

def setUpCall(from_state, numbers):
	if len(numbers) < 2 or not 0 <= from_state < 2:
		print "error: not enough numbers for conference"
		return -1
	global states
	global room_number
	global client
	room = "pr"+ str(room_number)
	room_number += 1
	if room_number > 100000:
		room_number = 0;
	for num in numbers: 
		num = cleanUpNum(num)
		if len(num) == 10 and num.isdigit():
			call = client.calls.create(to= "+1" + num,
						from_=states[from_state],
						url="http://twimlets.com/conference?Name=" + room + "&Message=%20")
		else:
			raise IOException('Bad input')
	return call.sid

def killCall(call_id):
	call = client.calls.update(call_id, status="completed")
	print call.start_time

def cleanUpNum(num):
	num = num.translate(None, '()-')
	return num

#nums = ["+19085287844", "+16107616189", "+17326681916", "+17324850325"]
# resources = client.calls.list()

