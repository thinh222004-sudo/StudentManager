class Payment:
    def __init__(self, booking, amount):
        self.booking = booking
        self.amount = amount
        
    def process_payment(self):
        print(f"Processing payment of ${self.amount} for booking ID {self.booking.booking_id}")
        print("Payment successful!")