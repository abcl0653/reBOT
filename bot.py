from flask import Flask, request, jsonify 
import json 
import os
import requests

headers = {
  'Accept': "application/json",
  'cache-control': "no-cache",
  #'Postman-Token': "9daaa16f-4745-4d4b-9582-032d69363d9f"
  }
auth = ('CAIC','Abcd1234$')

app = Flask(__name__) 
port = os.getenv("PORT")
#app.config['JSON_SORT_KEYS'] = False
@app.route('/customer', methods=['GET']) 
def index(): 
#  print(json.loads(request.get_data())) 

  url = "https://i039497trial-trial.apim1.hanatrial.ondemand.com/i039497trial/v1/customer/ZTEST_BP_CUST?$top=3&" + \
    "$filter=zprojectno eq 'Z/000-400'"
# querystring = {"$top":"3","$filter":"zprojectno%20eq%20%27Z/000-400%27"}
 
  response    = requests.get(url,headers = headers, auth = auth) 
  replies     = []
  elementList = []
  buttonList  = []

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

@app.route('/customer', methods=['POST']) 
def index1(): 
  #requestContent = json.loads(request.get_data())
  name        = request.values.get("person")
  mob_number  = request.values.get("mob_number")
  project     = request.values.get('project')
  requestContent = {}
  requestContent['BP'] = {}
  requestContent['BP']['BP_K'] ={}
  requestContent['BP']['BP_P'] ={}

  requestContent['BP']['BP_K']['ZPROJECTNO'] = project
  requestContent['BP']['BP_K']['NAME']       = name
  requestContent['BP']['BP_K']['CUSTOMER_TYPE'] = '10'
  requestContent['BP']['BP_K']['MOB_NUMBER']    = mob_number
  requestContent['BP']['BP_P']['ZPROJECTNO'] = project

  url2 = "https://i039497trial-trial.apim1.hanatrial.ondemand.com/i039497trial/v1/create_cust"
  print(json.dumps(requestContent))
  response = requests.post(url2, data = json.dumps(requestContent),headers = headers, auth = auth) 
  #print(response.json())
  return jsonify(
    status = 200,conversation={
      'memory':{'partner':response.json()['BP']['BP_K']['PARTNER']}
    }
  )
 
app.run(host='0.0.0.0',port=port)
