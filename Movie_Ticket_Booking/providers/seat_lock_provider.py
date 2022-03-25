from abc import ABC, abstractmethod


class SeatLockProvider(ABC):
    """
    Seat Lock Provider Interface, can be implemented in multiple ways
    """

    @abstractmethod
    def lock_seats(self, user, show, seats):
        pass

    @abstractmethod
    def unlock_seats(self, user, show, seats):
        pass

    @abstractmethod
    def validate_lock(self, user, show, seat):
        pass
