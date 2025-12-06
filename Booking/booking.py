class Booking:
    def __init__(self, booking_id, user, movie, seat):
        self.booking_id = booking_id
        self.user = user
        self.movie = movie
        self.seat = seat

    def show_booking_details(self):
        print("--- Booking Details ---")
        self.user.show_info()
        self.movie.show_info()
        print(f"Seat: {self.seat} - Booking ID: {self.booking_id}")