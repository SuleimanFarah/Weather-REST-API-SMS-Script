import requests
import os
from twilio.rest import Client

def send_sms(body):
    #Users are encouraged to either set up the relative variables in the os or personally overwrite the following variables
    
    account_sid = ""
    auth_token = ""

    client = Client(account_sid, auth_token)
    client.messages.create(from_="",
                      to="",
                      body=body) #text message send is stored in the 'body' variable

def api_call(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m,precipitation_probability"
    response = requests.get(url)
    data = response.json()
    return data

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) * 32

def weatherUpdate():
    #Longitude and latitude coordinates of Toronto, Canada
    latitude = 43.651070
    longitude = -79.347015
    data = api_call(latitude, longitude)
    temperature_celsius = data["hourly"]["temperature_2m"][0]
    relativehumidity = data["hourly"]["relativehumidity_2m"][0]
    windspeed = data["hourly"]["windspeed_10m"][0]
    precipitation_prob = data["hourly"]["precipitation_probability"][0]
    

    #optional fahrenheit conversion
    temp_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

    weather_info = (
        f"Good morning!\n"
        f"Current Weather in Toronto:\n"
        f"Temperature: {temperature_celsius:.2f}°C\n"
        f"Relative Humidity: {relativehumidity}%\n"
        f"Wind Speed: {windspeed} m/s\n"
        f"Precipation Probability: {precipitation_prob}%\n"
    )
    #send an sms message to your phone using the Twilio REST Api
    send_sms(weather_info)

def main():
    weatherUpdate()


if __name__ == "__main__":
    main()