from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import json

def sendSMS():
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = '' #enter account sid here
    auth_token = '' #enter auth token here
    client = Client(account_sid, auth_token)

    twilio_number = '' #enter twilio phone number here
    personal_number = '' #enter personal phone number here

    customerInformation = json.load(open('data.json', 'r'))
    name = customerInformation['name']
    phone = customerInformation['phone']
    message = 'Hello ' + name + '!'

    message = client.messages.create(
                                body=message,
                                from_=twilio_number,
                                to=personal_number
                            )

    print(message.sid)
    return

def generateResponse():
    return

