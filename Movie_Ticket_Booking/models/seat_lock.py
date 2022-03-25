import datetime


class SeatBooking:

    def __init__(self, seat, show, locked_by, time_out_in_sec):
        self.__seat = seat
        self.__locked_by = locked_by
        self.__show = show
        self.__time_out_in_sec = time_out_in_sec
        self.__lock_time = datetime.datetime.now()

    def has_lock_expired(self):
        expire_time = self.__lock_time + datetime.timedelta(seconds=self.__time_out_in_sec)
        return expire_time < datetime.datetime.now()
