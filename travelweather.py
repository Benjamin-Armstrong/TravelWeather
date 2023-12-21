import requests

#Define function that gets longitude and latitude
def get_location(api_key, city, state, country):
    url_base = "http://api.openweathermap.org/geo/1.0/direct"
    param = {
        'q' : f'{city},{state},{country}',
        'limit' : 1,
        'appid' : api_key
    }
    
    # Request data from openweathermap API
    response = requests.get(url_base, param=param)
    
    # Check if location was found
    if response.status_code == 200:
        # Parse through the json response
        location_data = response.json()
        
        # Extra longitude and Latitude data        
        longitude = location_data
    
    
    

#Define function that gets weather data
def get_weather(api_key, location, date):
    url_base = "https://api.openweathermap.org/data/3.0/onecall"
    param = {
        'lat' : location[0],
        'lon' : location[1],
        'exclude' : "",
        'appid' : api_key
    }
    
    # Request data from openweathermap API
    response = requests.get(url_base, param=param)