import datetime

class Customer:
    NextTicket = 1

    def __init__(self, name: str, reason: str):
        self.ticket = Customer.NextTicket
        Customer.NextTicket += 1

        self.name = name
        self.reason = reason
        self.arrival = datetime.datetime.now()

    def __repr__(self):
        return f"Customer(ticket={self.ticket}, name='{self.name}', reason='{self.reason}')"
