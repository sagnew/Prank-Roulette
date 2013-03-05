from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import os
import twilio_wrapper

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/prank', methods=['POST', 'GET'])
def prank():
    userNumber = request.form['userNumber']
    call1 = request.form['caller1']
    call2 = request.form['caller2']
    call3 = request.form['caller3']
    call4 = request.form['caller4']
    call5 = request.form['caller5']
    potentialCallers = [userNumber, call1, call2, call3, call4, call5]
    callers = []
    state = request.form['states']

    for caller in potentialCallers:
        if not caller == "":
            callers.append(str(caller))

    print callers
    twilio_wrapper.setUpCall(int(state), callers)
    return render_template('index.html')

@app.route('/donate', methods=['POST', 'GET'])
def donate():
    return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug="true")

