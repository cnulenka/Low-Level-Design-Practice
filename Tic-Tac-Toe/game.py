from player import Player, HumanPlayer, ComputerPlayer
from check_win_stratergy import ICheckWinStrategy, OnlyDiagonalCheckWinStrategy
from board import Board


class Game:
    def __init__(
        self,
        size: int,
        first_player: Player,
        second_player: Player,
        win_strategy: ICheckWinStrategy,
    ):
        self.first_player = first_player
        self.second_player = second_player

        self.curr_player = None

        self.board = Board(size)

        self.win_strategy = win_strategy
        self.max_moves = size**2

    def set_current_player(self):
        # return current_payer
        self.curr_player = self.first_player
        pass

    def add_move_to_board(self, move):
        # update board with move
        pass

    def run(self):

        num_move = 0

        while num_move < self.max_moves:

            self.set_current_player()

            move = self.curr_player.make_move(self.board)
            self.add_move_to_board(move)

            win = self.win_strategy.check_win(self.board)

            if win:
                return f"{self.curr_player} you win !!"

        return "Draw!!"


player1 = HumanPlayer()
easy_algo = EasyMakeMoveStrategy()
player2 = ComputerPlayer(Symbol.RECTANGLE, "pooh", easy_algo)

win_strategy = OnlyDiagonalCheckWinStrategy()

game = Game(player1, player2, win_strategy)
game.run()
