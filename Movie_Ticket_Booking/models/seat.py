import uuid


class Seat:

    def __init__(self, row_num, col_num):
        self.__id = uuid.uuid4()
        self.__row_num = row_num
        self.__col_num = col_num

    def get_row_num(self):
        return self.__row_num

    def get_col_num(self):
        return self.__col_num
