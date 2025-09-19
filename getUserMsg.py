from flask import Flask, request
from twilio import twiml


app1 = Flask(__name__)


@app1.route('/', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    print(resp)
    return str(resp)

if __name__ == '__main__':
    app1.run()