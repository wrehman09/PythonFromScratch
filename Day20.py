#API's


from symbol import parameters
import requests

response=requests.get("http://api.open-notify.org/iss-now.json")

#response.raise_for_status()   Raise exception in case of unsuccessfull

data=response.json()
print(data)



# kanya quote api

response=requests.get(url="https://api.kanye.rest/")
quote=response.json()
print(quote["quote"])


#api request with parameters 

parameters={
    "lat":"28.984463",
    "lng":"77.706413",
    "formatted":"0"
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

print(response.text)