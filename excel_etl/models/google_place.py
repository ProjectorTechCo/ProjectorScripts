from excel_etl.models.model import  GoogleModel


class GooglePlace(GoogleModel):
    def __init__(self, address, longitude, latitude, name):
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.name = name
