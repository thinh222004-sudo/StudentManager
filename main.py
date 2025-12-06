from User.user import User
from Movie.movie import Movie
from Booking.booking import Booking
from Payment.payment import Payment

def main():
    user1 = User("U001", "Nguyen Dinh Thinh")
    user2 = User("U002", "Nguyen Phuoc Datbeheading")

    user1.show_info()
    user2.show_info()
    print("\n")

    movie1 = Movie("M01", "Doraemon: Nobita's Earth Symphony", 110)
    movie2 = Movie("M02", "Godzilla x Kong: The New Empire", 115)

    movie1.show_info()
    movie2.show_info()
    print("\n")

    booking1 = Booking("B123", user1, movie1, "A5")
    booking1.show_booking_details()
    booking2 = Booking("B124", user2, movie2, "C2")
    booking2.show_booking_details()
    print("\n")
    
    payment1 = Payment(booking1, 9.99)
    payment1.process_payment()

if __name__ == "__main__":
    main()


#aaa
#bbb
#ccc