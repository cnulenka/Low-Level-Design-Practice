import uuid


class Screen:

    def __init__(self, name, theatre):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__seats = []
        self.__theatre = theatre

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_theatre(self):
        return self.__theatre

    def add_seat(self, seat):
        self.__seats.append(seat)
