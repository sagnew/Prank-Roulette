import os
import re

import twilio.twiml
from flask import Flask, render_template, request
from twilio.util import TwilioCapability
from werkzeug.contrib.fixers import ProxyFix

import twilio_wrapper as twrapper

app = Flask(__name__)

caller_id = ['+14846854944', '+14159686840']
default_client = "JohnCorndog"
room = 0
error = """<?xml version="1.0" encoding="UTF-8" ?>
        <Response>
        <Say>Invalid Input</Say>
        </Response>
        """
account_sid = os.environ.get('ACCOUNT_SID', None)
auth_token = os.environ.get('AUTH_TOKEN', None)
application_sid = os.environ.get('APP_SID', None)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    """Respond to incoming requests."""
    capability = TwilioCapability(account_sid, auth_token)

    capability.allow_client_outgoing(application_sid)
    token = capability.generate()

    return render_template('index.html', token=token)


@app.route('/voice', methods=['POST', 'GET'])
def voice():
    number1 = request.values.get('PhoneNumber1', None)
    number2 = request.values.get('PhoneNumber2', None)
    state = int(request.values.get('State', 0))
    resp = twilio.twiml.Response()

    global error
    global room
    if room > 100000:
        room = 0

    room += 1
    numbers = []
    theNums = [number1, number2]

    for num in theNums:
        if num is not None and re.search('^[\d\(\)\- \+]+$', num):
            numbers.append(num)
    if len(numbers) < 2:
        return error

    # Nest <Client> TwiML inside of a <Dial> verb
    with resp.dial(callerId=caller_id[0]) as r:
        r.conference('pr' + str(room))

    sid = twrapper.setUpCall(state, numbers, 'pr' + str(room))

    if sid == -1:
        return "llderp"
    return str(resp)


@app.route('/donate', methods=['POST', 'GET'])
def donate():
    return render_template('index.html')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
