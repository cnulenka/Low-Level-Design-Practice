import uuid


class Movie:

    def __init__(self, name):
        self.__id = uuid.uuid4()
        self.__name = name

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id
