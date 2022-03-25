import uuid
from Movie_Ticket_Booking.constants import BookingStatus
from Movie_Ticket_Booking.exceptions import InvalidStateException

class Booking:

    def __init__(self, show, booked_seats):
        self.__id = uuid.uuid4()
        self.__show = show
        self.__booked_seats = booked_seats
        self.__status = BookingStatus.CREATED

    def is_confirmed(self):
        return self.__status == BookingStatus.CONFIRMED

    def confirm_booking(self):
        if self.__status != BookingStatus.CREATED:
            raise InvalidStateException("Booking can only be confirmed after creation.")
        self.__status = BookingStatus.CONFIRMED

    def expire_booking(self):
        if self.__status != BookingStatus.CREATED:
            raise InvalidStateException("Booking can only be expired after creation.")
        self.__status = BookingStatus.EXPIRED
