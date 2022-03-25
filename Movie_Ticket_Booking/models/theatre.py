import uuid


class Theatre:

    def __init__(self, name, theatre):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__screens = []

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def add_screens(self, screen):
        self.__screens.append(screen)
