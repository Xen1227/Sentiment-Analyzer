import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
from pprint import pprint

#calls Microsoft's sentiment analysis API on the text message and returns the sentiment score
def performNLP(message):
    subscription_key = '' #enter Microsoft Azure subscription key here
    url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
    documents = {'documents' : [
    {'id': '1', 'language': 'en', 'text': message}
    ]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(url, headers=headers, json=documents)
    sentiments = response.json()
    score = sentiments['documents'][0]['score']
    pprint(sentiments)
    return score
