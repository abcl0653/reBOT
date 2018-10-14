import requests

url = "https://i039497trial-trial.apim1.hanatrial.ondemand.com/i039497trial/v1/customer/ZTEST_BP_CUST?$top=3&$filter=zprojectno eq 'Z/000-400'"
querystring = {"$top":"3","$filter":"zprojectno eq Z/000-400"}

headers = {
  'Accept': "application/json",
  'cache-control': "no-cache",
  'Authorization': "Basic Q0FJQzpBYmNkMTIzNCQ="
  #'Postman-Token': "9daaa16f-4745-4d4b-9582-032d69363d9f"
  }
auth = ('CAIC','Abcd1234$')

response = requests.get(url,headers = headers, auth=('CAIC','Abcd1234$'))

print response.text