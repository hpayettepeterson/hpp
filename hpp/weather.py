#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
import requests



BASE_URI = "https://www.metaweather.com"


def search_city(query):
    cityurl = f"https://www.metaweather.com/api/location/search/?query={query.strip()}"
    cityresponse = requests.get(cityurl).json()
    #print(cityresponse)
    if cityresponse == []:
        return print(f"Error: no known city \"{query}\"")
    if len(cityresponse) > 1:
        list_response = [cityresponse[i]['title'] for i in range(len(cityresponse))]
        return print(f"There are several options, please type one of the following: {str(list_response).lstrip('[').rstrip(']')}")
    return cityresponse



def weather_forecast(woeid, city):
    print(f"here's the weather in {city}")
    weatherurl = f"https://www.metaweather.com/api/location/{woeid}/"
    weatherresponse = requests.get(weatherurl).json()
    forecast = []
    for list1 in weatherresponse['consolidated_weather']:
        date = list1['applicable_date']
        weather = list1['weather_state_name']
        temphigh = list1['max_temp']
        forecast.append([date, weather, temphigh])
        #forecast = f'''
        #      Date: {date}
        #      Weather: {weather}
        #      High Temp (Celsius): {round(temphigh)}
        #      '''
    return forecast


def forecast():
    '''Ask user for a city and display weather forecast'''
    query = 'Berlin'
    cityresponse = search_city(query)
    if type(cityresponse) == list:
        city = cityresponse[0]['title']
        woeid = cityresponse[0]['woeid']
        #print(type(weather_forecast))
        #print(weather_forecast(woeid, city))
        #print(type(weather_forecast))
        fivedayforecast = weather_forecast(woeid, city)
        for i in range(len(fivedayforecast)):
            print(f'''
                  date: {fivedayforecast[i][0]}
                  weather: {fivedayforecast[i][1]}
                  high temp: {round(int(fivedayforecast[i][2]))}''')






# if __name__ == '__main__':
#     try:
#         while True:
#             main()
#     except KeyboardInterrupt:
#         print('\nGoodbye!')
#         sys.exit(0)
