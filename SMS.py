import requests
import json
URL = 'https://www.way2sms.com/api/v1/sendCampaign'
# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
# get response
response = sendPostRequest(URL, 'XOMKQLFMYQKJHYWZIJ1UIL9DM59YOTQJ', 'XG4WY4HXVXDUHS7Z', 'stage', '9030918161', 'komirishettyvinaykmr47@gmail.com', 'hello don lal darwaza' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)
