# import os
# from flask import Flask, render_template, request
# from twilio.rest import Client

# # app1 = Flask(__name__)

# account_sid = 'AC6712ce5c48f555eeb9f3fa074bb0fa84'
# auth_token = '8c855121f4cdf1ff643a817c1661ba1f'
# client = Client(account_sid, auth_token)

# phone_number = '+14252410084'
# message = client.messages.create(
#   from_='+18559451964',
#   body='Tell me something you are proud of today.',
#   to=phone_number
# )

# print(message.sid)

# # import os
# # from twilio.rest import Client

# # account_sid = 'AC6712ce5c48f555eeb9f3fa074bb0fa84'
# # auth_token = '8c855121f4cdf1ff643a817c1661ba1f'
# # client = Client(account_sid, auth_token)

# # client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
# #                       to=os.environ.get('CELL_PHONE_NUMBER'),
# #                       body='You just sent an SMS from Python using Twilio!')

# # # Route to handle incoming SMS messages
# # @app1.route('/')
# # def sms():
# #     # Send a specific message to the user
# #     message = client.messages.create(
# #         from_='+18559451964',
# #         body='Tell me something you are proud of today',
# #         to='+14252410084'
# #     )

# #     # Return an empty response
# #     return render_template('file.html')

# # if __name__ == '__main__':
# #     app1.run(debug=True)
    
# # # app = Flask(__name__)

# # print('hello')

# # from twilio.twiml.messaging_response import MessagingResponse
# # app = Flask(__name__)
# # @app.route('/sms', methods=['POST'])
# # def sms():
# #     # Get the user's phone number from the incoming message
# #     phone_number = request.values.get('From', None)

# #     # Get the user's message body
# #     message_body = request.values.get('Body', None)

# #     # Do something with the user's message
# #     response_body = f'You said: {message_body}'

# #     # Send a response back to the user
# #     resp = MessagingResponse()
# #     resp.message(response_body)
# #     return str(resp)


# # message = client.messages.create(
# #   from_='+18559451964',
# #   body=message_body,
# #   to=phone_number
# # )

# from flask import Flask, request
# from twilio import twiml


# app = Flask(__name__)


# @app.route('/hidden', methods=['POST'])
# def sms():
#     number = request.form['From']
#     message_body = request.form['Body']

#     resp = twiml.Response()
#     resp.message('Hello {}, you said: {}'.format(number, message_body))
#     print(resp)
#     return render_template('/hidden', output=resp)

# if __name__ == '__main__':
#     app.run()


