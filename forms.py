from AQI_WebApp_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField

class AQIParameters(FlaskForm):
    aqiparameter = SelectField('data', choices=[("Location", "Coordinates"),
                                                ("Current", "Weather"),
                                                ("Pollution", "Pollution")])

    '''
    Complete this class with the appropriate parameters inside SelectField for the dropdown menu
    '''

def aqi_parameter():
    url = "https://api.airvisual.com/v2/nearest_city?key="
    aqi_key = main_functions.read_from_file("JSON_Files/aqi_key.json")
    aqi_key = aqi_key['aqi_key']

    url2 = url+aqi_key

    request_json = requests.get(url2).json()

    main_functions.save_to_file(request_json, "JSON_Files/aqi.json")

    air_quality_index = main_functions.read_from_file("AQI_WebApp_Flask/JSON_Files/aqi.json")

    '''
    From the json file read above, please find the right values for the variables below
    Notice that I already accessed the values for latitude and longitude
    and I also concatenated them into one variable called coordinates
    '''

    latitude = air_quality_index['data']['location']['coordinates'][0]
    longitude = air_quality_index['data']['location']['coordinates'][1]
    coordinates = str(latitude)+', '+str(longitude)

    temperatureC = air_quality_index['current']['weather']['tp']
    pressure = air_quality_index['current']['weather']['pr']
    humidity = air_quality_index['current']['weather']['hu']
    aqius = air_quality_index['pollution']['aqius']

    parameters = {'coordinates': coordinates,
                  'temperatureC': str(temperatureC),
                  'pressure': str(pressure),
                  'humidity': str(humidity),
                  'aqius': str(aqius)}
    return parameters

