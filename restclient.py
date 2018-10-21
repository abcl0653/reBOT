# Call REST service Test
from flask import Flask, request, jsonify 
import json 
import os
import requests

headers = {
  "Accept": "application/json",
  "cache-control": "no-cache",
  #"Postman-Token": "9daaa16f-4745-4d4b-9582-032d69363d9f"
  }
auth = ("CAIC","Abcd1234$")

requestContent = {}
requestContent["BP"] = {}
requestContent["BP"]["BP_K"] ={}
requestContent["BP"]["BP_P"] ={}

requestContent["BP"]["BP_K"]["ZPROJECTNO"] = "Z001"
requestContent["BP"]["BP_K"]["NAME"]       = "Jerry Seinfeld"
requestContent["BP"]["BP_K"]["CUSTOMER_TYPE"] = "10"
requestContent["BP"]["BP_K"]["MOB_NUMBER"]    = "19992939293928"
requestContent["BP"]["BP_P"]["ZPROJECTNO"] = "Z001"

print(json.dumps(requestContent))

url2 = "https://i039497trial-trial.apim1.hanatrial.ondemand.com/i039497trial/v1/create_cust"
response = requests.post(url2, data = json.dumps(requestContent),headers = headers, auth = auth) 
print(response)