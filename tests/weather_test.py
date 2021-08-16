from hpp.weather import weather_forecast

def weather_test():
    assert type(weather_forecast()) == list
