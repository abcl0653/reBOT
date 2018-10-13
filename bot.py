from flask import Flask, request, jsonify 
import json 
import os

app = Flask(__name__) 
port = os.getenv("PORT")
#app.config['JSON_SORT_KEYS'] = False
@app.route('/', methods=['POST']) 
def index(): 
  print(json.loads(request.get_data())) 
  
  replies = []
  elementList =[]

  buttonList = []

  buttonTitle = '+86 18621339999'
  buttonValue = '+86 18621339999'
  buttontype = 'phonenumber'
  button = {"title":buttonTitle,"value":buttonValue,"type":buttontype}
  buttonList.append(button)

  customerName = 'Mr. George Costanza'
  customerIntention = 'Intention 10%'
  imageUrl = './George-costanza.jpg'
  element = {"title":customerName,"subtitle":customerIntention,
    "buttons":buttonList,
    "imageUrl":imageUrl}

  elementList.append(element) # append more elements to form a richer list

  customerName = 'Ms. Elaine Benes'
  customerIntention = 'Intention 80%'
  imageUrl = './Elaine.jpg'
  element = {"title":customerName,"subtitle":customerIntention,
    "buttons":buttonList,
    "imageUrl":imageUrl}

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
 
app.run(host='0.0.0.0',port=port)
