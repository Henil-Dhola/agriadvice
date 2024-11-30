import requests

def get_weather(city_name):
    api_key = 'd6eb14d6040fc4c1f15f9059f88c97ec'  # Your API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Get temperature in Celsius
    }

    try:
        # Making the API request
        response = requests.get(base_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the relevant information
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'clouds': data['clouds']['all'],
                'description': data['weather'][0]['description'],
                'rain': data.get('rain', {}).get('1h', 0),  # Rain volume in last 1 hour (if available)
                'snow': data.get('snow', {}).get('1h', 0),  # Snow volume in last 1 hour (if available)
            }
            return weather
        else:
            return {'error': f"City {city_name} not found or another error occurred."}
    except Exception as e:
        return {'error': f"An error occurred: {str(e)}"}
