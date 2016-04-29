import requests
import json

ip=""
mac=""
user=""
password=""
url= "http://"+ip+"/api/location/v1/clients/"+mac

response= requests.get(url, auth=(user, password))
jresponse= response.json()
status = response.status_code

if  status>= 200 and status < 300:

	if jresponse["dot11Status"] == "ASSOCIATED":
		print "The client "+mac+" is currently associated"

	else:
		print "Something is wrong. the dot11Status is "+jresponse["dot11Status"]
	 
else:
	print "The API request was not successful"
	print status