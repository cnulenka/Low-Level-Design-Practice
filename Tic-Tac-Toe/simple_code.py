class Game:
    def __init__(self, size):
        self.size = size
        # 2D matrix/char array, N*N
        self.grid = [["" for _ in range(size)] for _ in range(size)]

    def check_win(self):
        # win check algorithm
        # returns true/false
        pass

    def run(self):
        num_move = 0
        max_move = self.size**2  # N*N

        while num_move < max_move:
            i, j = input()  # get i,j from stdin

            if num_move % 2 == 0:  # if even turn
                self.grid[i][j] = "O"
            else:
                self.grid[i][j] = "X"  # odd turn

            if self.check_win():
                print("Congrats, you win!!")
                return

            num_move += 1

            # if no winners
        print("Draw!!")
