class Model(object):
    def to_dict(self):
        return {key: value.to_dict() if issubclass(type(value), Model) else value
                for key, value in self.__dict__.items()}


class GeoLocation(Model):
    def __init__(self, geometry: dict):
        self.longitude = geometry.get('lng')
        self.latitude = geometry.get('lat')
