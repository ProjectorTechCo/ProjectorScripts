from excel_etl.models import Model, GeoLocation


class GoogleNearbyPlace(Model):
    def __init__(self, geo_location, place_id, types, name):
        self.geo_location = GeoLocation(geo_location)
        self.place_id = place_id
        self.types = types
        self.name = name
