import requests
import os
from urllib.parse import urlencode

from excel_etl.models.google_nearby_place import GoogleNearbyPlace
from excel_etl.models.google_place import GooglePlace

API_KEY = os.environ.get('GOOGLE_API_KEY') or ''
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
    return GooglePlace(address=address_info.get('formatted_address'), geolocation=location,
                       name=address_info.get('name')).to_dict()


def find_close_places(latitude, longitude, radius):
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius
    }

    res = requests.get(generate_api_url(api_type='place', api_function='nearbysearch', params=params))
    content = res.json()
    if res.status_code != 200 or content.get('status') != 'OK':
        raise GooglePlaceException(content)

    return [GoogleNearbyPlace(geo_location=place.get('geometry').get('location'), place_id=place.get('place_id'),
                              types=place.get('types'), name=place.get('name')).to_dict() for place in
            content.get('results')]
