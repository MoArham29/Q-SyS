import datetime

class Customer:
    NextTicket = 1

    def __init__(self, name, reason, phone, email):
        self.ticket = Customer.NextTicket
        Customer.NextTicket += 1

        self.name = name
        self.reason = reason
        self.phone = phone
        self.email = email
        self.arrival = datetime.datetime.now()

    def __repr__(self):
        return (f"Customer(ticket={self.ticket}, name='{self.name}', "
                f"phone='{self.phone}', email='{self.email}')")
