from excel_etl.models import Model, GeoLocation


class GooglePlace(Model):
    def __init__(self, address, geolocation, name):
        self.address = address
        self.geolocation = GeoLocation(geolocation)
        self.name = name
