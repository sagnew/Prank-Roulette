from flask import Flask
from flask import render_template
from flask import request
from twilio.util import TwilioCapability
import twilio.twiml
import twilio_wrapper as twrapper
import os
import re

app = Flask(__name__)

caller_id = ['+14846854944', '+14159686840']
default_client = "JohnCorndog"
room = 0
error = """<?xml version="1.0" encoding="UTF-8" ?>
        <Response>
        <Say>Invalid Input</Say>
        </Response>
        """


@app.route('/')
def main_page():
    """Respond to incoming requests."""
    account_sid = "Stop trying to read our shit!"
    auth_token = "Seriously thats not cool..."

    capability = TwilioCapability(account_sid, auth_token)

    # This is a special Quickstart application sid - or configure your own
    # at twilio.com/user/account/apps
    application_sid = "APaf6c7ab08a32e7fb541a78d97d592100"
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()

    return render_template('index.html', token=token)


@app.route('/voice')
def voice():
    number1 = request.values.get('PhoneNumber1', None)
    number2 = request.values.get('PhoneNumber2', None)
    number3 = request.values.get('PhoneNumber3', None)
    number4 = request.values.get('PhoneNumber4', None)
    number5 = request.values.get('PhoneNumber5', None)
    state = int(request.values.get('State', None))
    #cid = request.values.get('state', None)
    resp = twilio.twiml.Response()

    global error
    global room
    if room > 100000:
        room = 0

#'[0-9]{10}'
    room += 1
    numbers = []
    theNums = [number1, number2, number3, number4, number5]

    for num in theNums:
        if num is not None and re.search('^[\d\(\)\- \+]+$', num):
            numbers.append(num)
    if len(numbers) < 2:
        return error

    for num in numbers:
        print num

    # Nest <Client> TwiML inside of a <Dial> verb
    with resp.dial(callerId=caller_id[0]) as r:
        r.conference('pr' + str(room))

    sid = twrapper.setUpCall(state, numbers, 'pr' + str(room))

    if sid == -1:
        return "llderp"
    return str(resp)


#@app.route('/prank', methods=['POST', 'GET'])
#def prank():
#    userNumber = request.form['userNumber']
#    call1 = request.form['caller1']
#    call2 = request.form['caller2']
#    call3 = request.form['caller3']
#    call4 = request.form['caller4']
#    call5 = request.form['caller5']
#    potentialCallers = [userNumber, call1, call2, call3, call4, call5]
#    callers = []
#    state = request.form['states']
#
#    for caller in potentialCallers:
#        if not caller == "":
#            callers.append(str(caller))
#
#    print callers
#    print state
#    #twilio_wrapper.setUpCall(int(state), callers)
#    return render_template('prank.html')
#

@app.route('/donate', methods=['POST', 'GET'])
def donate():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="true")
