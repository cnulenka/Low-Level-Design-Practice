from abc import ABC, abstractmethod
from board import Board


class ICheckWinStrategy(ABC):
    @abstractmethod
    def check_win(self, board: Board):
        # must be implemented by child classes
        pass


class StandardCheckWinStrategy(ICheckWinStrategy):
    def check_win(self, board: Board):
        # implement standard algorithm
        # to check winner
        pass


class OnlyDiagonalCheckWinStrategy(ICheckWinStrategy):
    def check_win(self, board: Board):
        # implement only diagonal algorithm
        # to check winner
        pass
