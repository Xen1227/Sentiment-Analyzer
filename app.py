from flask import Flask
from flask import render_template
from flask import request
from sendSMS import sendSMS, generateResponse
from runNLP import performNLP
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Sentiment Analyzer!"

@app.route('/Dashboard')
def signUp():
    with open('response.json', 'w') as outfile:
        json.dump({'response':" ",'sentiment':" "}, outfile)
    return render_template('Dashboard.html')

@app.route('/Analysis')
def goToAnalysisPage():
    return render_template('Analysis.html')

@app.route('/processResponse', methods=['POST'])
def processResponse():
    customerInformation = json.load(open('response.json', 'r'))
    response = customerInformation['response']
    sentiment = customerInformation['sentiment']

    if (response == " "):
        results = ""
    else:
        results = response + ',' + sentiment
    with open('response.json', 'w') as outfile:
        json.dump({'response':customerInformation['response'],'sentiment':customerInformation['sentiment']}, outfile)
    return results

@app.route('/SendSMS', methods=['POST'])
def signUpUser():
    name =  request.form['name']
    phone = request.form['phone']
    with open('data.json', 'w') as outfile:
        json.dump({'name':name,'phone':phone}, outfile)
    sendSMS()
    return json.dumps({'status':'OK','name':name,'phone':phone})

@app.route("/sms", methods=['GET', 'POST'])
def sendResponse():

    # Start our response
    body = request.values.get('Body', None)
    print(body)
    score = performNLP(body)
    resp = MessagingResponse()

    # Add a message
    sentiment = ""
    print(score)

    if (score >= 0.5):
        sentiment = "Positive sentiment"
    else:
        sentiment = "Negative sentiment"

    resp.message(sentiment)

    with open('response.json', 'w') as outfile:
        json.dump({'response':body,'sentiment':sentiment}, outfile)
    
    return str(resp)


if __name__ == "__main__":
    app.run()