import os
import re

import twilio.twiml
from flask import Flask, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

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
    return render_template('index.html')


@app.route('/makecall', methods=['POST'])
def make_call():
    """Initiate the prank call."""
    number1 = request.form.get('PhoneNumber1', None)
    number2 = request.form.get('PhoneNumber2', None)
    state = int(request.form.get('State', 0))
    
    if not number1 or not number2:
        return "Error: Both phone numbers required", 400
    
    global room
    if room > 100000:
        room = 0
    room += 1
    
    result = twrapper.setUpCall(state, [number1, number2], 'pr' + str(room))
    
    if result == -1:
        return "Error setting up call", 500
    
    return {"status": "success", "message": "Calls initiated"}



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
        if num is not None and re.search(r'^[\d\(\)\- \+]+$', num):
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
