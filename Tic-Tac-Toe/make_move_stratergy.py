from abc import ABC, abstractmethod
from board import Board


class IMakeMoveStrategy(ABC):
    # interface, blueprint the methods
    # to be implemented

    @abstractmethod
    def make_move(self, board: Board):
        # must be implemented by child classes
        pass


class EasyMakeMoveStrategy(IMakeMoveStrategy):
    def make_move(self, board: Board):
        # implement easy algorithm
        # return move
        pass


class MediumMakeMoveStrategy(IMakeMoveStrategy):
    def make_move(self, board: Board):
        # implement medium algorithm
        # return move
        pass
