from flask import Flask,request,redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import settings

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    return 'Hello World!'


@app.route('/receive/',methods=['GET','POST'])
def receive():
    message = request.form['Body']
    resp = twilio.twiml.Response()
    if message.lower() == 'hello':
        resp.message('Hello from cs6432015 from IAN CARVALHO')
    else:
        resp.message('Please send a "hello"')
    return str(resp)

@app.route('/send/',methods=['GET','POST'])
def send():
    client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    txt = 'Hello from IAN CARVALHO'
    message = client.messages.create(to=settings.SEND_NUMBER, from_='+16466933151',
                                     body=txt)
    return 'Message sent to ' + number

if __name__ == '__main__':
    app.run(debug=True)
