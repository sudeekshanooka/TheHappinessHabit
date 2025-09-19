from flask import Flask, render_template, request
from twilio.rest import Client
from markupsafe import escape

app = Flask(__name__)

# Twilio account credentials
# account_sid = 'SKa0a8eb4236e6a61f4480511cf2f2a918'
# auth_token = '8c855121f4cdf1ff643a817c1661ba1f'

# # Twilio phone number
# twilio_number = 8559451964

# Initialize Twilio client
# client = Client(account_sid, auth_token)

# #Route to handle incoming SMS messages
# @app.route('/', methods=['POST'])
# def sms():
#     # Get the user's phone number from the incoming message
#     phone_number = request.form['From']

#     # Send a specific message to the user
#     message = 'Tell me something you are proud of today'
#     client.messages.create(
#         body=message,
#         from_=twilio_number,
#         to=phone_number
#     )

#     # Return an empty response
#     return render_template('index.html')

# # display the website
# from flask import Flask, render_template

# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# app = Flask(__name__)

import os

# app1 = Flask(__name__)

account_sid = 'AC6712ce5c48f555eeb9f3fa074bb0fa84'
auth_token = '8c855121f4cdf1ff643a817c1661ba1f'
client = Client(account_sid, auth_token)

phone_number = '+17633379467'
message = client.messages.create(
  from_='+18559451964',
  body='Tell me something you are proud of today.',
  to='+17633379467'
)

print(message.sid)

# import os
# from twilio.rest import Client

# account_sid = 'AC6712ce5c48f555eeb9f3fa074bb0fa84'
# auth_token = '8c855121f4cdf1ff643a817c1661ba1f'
# client = Client(account_sid, auth_token)

# client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
#                       to=os.environ.get('CELL_PHONE_NUMBER'),
#                       body='You just sent an SMS from Python using Twilio!')

# # Route to handle incoming SMS messages
# @app1.route('/')
# def sms():
#     # Send a specific message to the user
#     message = client.messages.create(
#         from_='+18559451964',
#         body='Tell me something you are proud of today',
#         to='+17633379467'
#     )

#     # Return an empty response
#     return render_template('file.html')

# if __name__ == '__main__':
#     app1.run(debug=True)
    
# # app = Flask(__name__)

# print('hello')

# from twilio.twiml.messaging_response import MessagingResponse
# app = Flask(__name__)
# @app.route('/sms', methods=['POST'])
# def sms():
#     # Get the user's phone number from the incoming message
#     phone_number = request.values.get('From', None)

#     # Get the user's message body
#     message_body = request.values.get('Body', None)

#     # Do something with the user's message
#     response_body = f'You said: {message_body}'

#     # Send a response back to the user
#     resp = MessagingResponse()
#     resp.message(response_body)
#     return str(resp)


# message = client.messages.create(
#   from_='+18559451964',
#   body='Tell me something you are proud of today!',
#   to=phone_number
# )

# from flask import Flask, request
# from twilio import twiml




# Run index.html page
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)

#COMMENTED OUT
# @app.route('/hidden', methods=['POST'])
# def sms():
#     number = request.form['From']
#     message_body = request.form['Body']

#     resp = twiml.Response()
#     resp.message('Hello {}, you said: {}'.format(number, message_body))
#     print(resp)
#     return render_template('/hidden')

# if __name__ == '__main__':
#     app.run()


# # display the website

# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# CHat gpt attempt


# app = Flask(__name__)

# @app.route('/hidden', methods=['POST'])
# def receive_sms():
#     # code to handle incoming SMS message
#     user_response = request.values.get('Body')
#     phone_number = request.values.get('From')
#     with open('templates/text.txt', 'w') as f:
#         f.write(user_response)
#     return ''

# print('hello')

# from flask import render_template

# @app.route('/')
# def show_responses():
#     responses = {}
#     for file_name in os.listdir('.'):
#         if file_name.endswith('.txt'):
#             with open(file_name) as f:
#                 responses[file_name] = f.read()
#     return render_template('responses.html', responses=responses)




app = Flask(__name__)

@app.route("/hidden", methods=['POST'])
def sms():
    print('hello')
    """Respond to incoming SMS with a message."""
    # Get the user's message from the incoming request
    incoming_message = request.form['Body']

    # Write the message to a file
    with open('template/text.txt', 'a') as f:
        f.write(incoming_message + '\n')

    # Generate a TwiML response

    MessagingResponse = client.messages.create(
    from_='+18559451964',
    body="Thanks for your message! We've saved it to our records.",
    to='+17633379467'
    )


    twiml = MessagingResponse()
    twiml.message("Thanks for your message! We've saved it to our records.")

    # Return the TwiML response
    return str(twiml)   

if __name__ == '__main__':
    app.run(debug=True)
