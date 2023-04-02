class Board:
    def __init__(self, size):

        self.size = size

        # 2D matrix/char array, N*N
        self.grid = [["" for _ in range(size)] for _ in range(size)]

        # self.color
