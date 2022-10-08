#api authentication , sending sms from twilio  environment variable for storing api key 
#  automatic rain aleert   

import requests  

parameters={
    "appid":"APPID",
    "q":"Meerut,India",
    "units":"metric"
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/weather",params=parameters)
data=response.json()
print(data)
weatherdata=data['weather'][0]['description']
temp=data['main']['temp']
print(temp)
print(weatherdata)

from datetime import datetime
from pytz import timezone
ts = int(data['sys']['sunrise'])
sunset=int(data['sys']['sunset'])

sunrise=datetime.fromtimestamp(ts).astimezone(timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
print(sunrise)
sunset=datetime.fromtimestamp(sunset).astimezone(timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
print(sunset)


import os
from twilio.rest import Client


account_sid =os.environ['twiliosid']
auth_token =  os.environ['twilioauthtoken']
client = Client(account_sid, auth_token)
bodys="Temp:"+str(temp)+" Weather condition: "+weatherdata +"  Sunrise:"+sunrise+" Sunset:"+sunset
message = client.messages.create(
                              body=bodys,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919027413884'
                          )

print(message.sid)
