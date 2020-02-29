class GooglePlace(object):
    def __init__(self, address, longitude, latitude, name):
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.name = name

    def to_dict(self):
        return self.__dict__.items()
