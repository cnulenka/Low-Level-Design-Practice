import uuid


class Show:

    def __init__(self, movie, screen, start_time, duration):
        self.__id = uuid.uuid4()
        self.__movie = movie
        self.__screen = screen
        self.__start_time = start_time
        self.__duration = duration


