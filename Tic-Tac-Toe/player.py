from abc import ABC, abstractmethod
from symbol import Symbol
from user import User
from board import Board
from make_move_stratergy import IMakeMoveStrategy, EasyMakeMoveStrategy


class Player(ABC):  # abstract
    def __init__(self, symbol: Symbol, user_name: str):
        self.symbol = symbol
        self.user_name = user_name

    @abstractmethod
    def make_move(self, board: Board):
        # return i, j
        pass


class HumanPlayer(Player):
    def __init__(self, symbol: Symbol, user_name: str, user: User):
        super().__init__(symbol, user_name)
        self.user = user

    def make_move(self, board: Board):
        # take input from stdin
        pass


class ComputerPlayer(Player):
    def __init__(
        self, symbol: Symbol, user_name: str, make_move_strategy: IMakeMoveStrategy
    ):
        super().__init__(symbol, user_name)
        self.make_move_strategy = make_move_strategy  # easy, medium, hard

    def make_move(self, board: Board):
        # based on strategy return move info
        return self.make_move_strategy.make_move(board)


easy_algo = EasyMakeMoveStrategy()
ComputerPlayer(Symbol.RECTANGLE, "pooh", easy_algo)
