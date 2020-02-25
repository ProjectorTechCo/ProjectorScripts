import requests
from urllib.parse import urlencode
import os

from ExcelETL.GooglePlace import GooglePlace

API_KEY = os.environ.get('GOOGLE_API_KEY')
MAPS_API = "https://maps.googleapis.com/maps/api/{api_type}/{api_function}/json?{params}&key=" + API_KEY


def generate_api_url(api_type, api_function, params):
    return MAPS_API.format(api_type=api_type, api_function=api_function, params=urlencode(params))


class GooglePlaceException(Exception):
    pass


def find_location_from_text(location_text):
    params = {
        "input": location_text,
        "inputtype": "textquery",
        "fields": "formatted_address,name,geometry"
    }
    res = requests.get(
        generate_api_url(api_type="place", api_function="findplacefromtext", params=params))
    content = res.json()
    if res.status_code != 200 or content.get('status') != 'OK':
        raise GooglePlaceException(content)

    # TODO: there can be many location in the 'candidates' field, find a way to handle it.
    address_info = content.get('candidates')[0]
    location = address_info.get('geometry').get('location')
    return GooglePlace(address=address_info.get('formatted_address'), longitude=location.get('lng'),
                       latitude=location.get('lat'), name=address_info.get('name'))
