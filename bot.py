from flask import Flask, request, jsonify 
import json 
import os
import requests

url = "https://i039497trial-trial.apim1.hanatrial.ondemand.com/i039497trial/v1/customer/ZTEST_BP_CUST?$top=3&$filter=zprojectno eq 'Z/000-400'"
# querystring = {"$top":"3","$filter":"zprojectno%20eq%20%27Z/000-400%27"}

headers = {
  'Accept': "application/json",
  'cache-control': "no-cache",
  #'Postman-Token': "9daaa16f-4745-4d4b-9582-032d69363d9f"
  }
auth = ('CAIC','Abcd1234$')

response = requests.get(url,headers = headers, auth = auth)

app = Flask(__name__) 
port = os.getenv("PORT")
#app.config['JSON_SORT_KEYS'] = False
@app.route('/', methods=['POST']) 
def index(): 
  print(json.loads(request.get_data())) 
  
  replies = []
  elementList =[]

  buttonList = []



  for bp in response.json()['d']['results']:
    
    customerName = bp['name'] #'Mr. George Costanza'
    customerIntention = 'Intention 10%'
    imageUrl = './George-costanza.jpg'
    element = {"title":customerName,"subtitle":customerIntention,
      "buttons":buttonList,
      "imageUrl":imageUrl}
    buttonTitle = bp['mob_number'] #'+86 18621339999'
    buttonValue = bp['mob_number'] #'+86 18621339999'
    buttontype = 'phonenumber'
    button = {"title":buttonTitle,"value":buttonValue,"type":buttontype}
    buttonList.append(button)

    elementList.append(element) # append more elements to form a richer list

  # customerName = 'Ms. Elaine Benes'
  # customerIntention = 'Intention 80%'
  # imageUrl = './Elaine.jpg'
  # element = {"title":customerName,"subtitle":customerIntention,
  #   "buttons":buttonList,
  #   "imageUrl":imageUrl}

  # elementList.append(element) # append more elements to form a richer list

  buttonList = []
  content = {"elements":elementList,"buttons":buttonList}
  reply = {"type":"list","content":content}
  replies.append(reply)

  return jsonify( 
    status=200, 
    replies = replies,

    conversation={ 
      'memory': { 'key': 'value' } 
    } 
  ) 
 
@app.route('/errors', methods=['POST']) 
def errors(): 
  print(json.loads(request.get_data())) 
  return jsonify(status=200) 
 
app.run(host='0.0.0.0',port=port)
