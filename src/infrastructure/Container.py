from infrastructure.SingletonMeta import SingletonMeta


class Container(metaclass=SingletonMeta):
    def __init__(self):
        self.services = {}

    def register(self, key, service):
        self.services[key] = service

    def get_service(self, key):
        return self.services.get(key)
