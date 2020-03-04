class GooglePlace(object):
    def __init__(self, address, longitude, latitude, name):
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.name = name

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items()}
