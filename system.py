
from customer import Customer
from QStructure import Queue

class QueueSystem:
    def __init__(self):
        self.queue = Queue()
        self.customers_by_ticket = {}

    def register_customer(self, name, reason):
        """Create and enqueue a new customer."""
        customer = Customer(name, reason)
        self.queue.enqueue(customer)
        self.customers_by_ticket[customer.ticket] = customer
        return customer

    def call_next(self):
        """Dequeue next customer."""
        next_customer = self.queue.dequeue()
        return next_customer

    def search_by_ticket(self, ticket_number):
        """Lookup customer by ticket."""
        return self.customers_by_ticket.get(ticket_number)

    def list_waiting(self):
        """Return a list of customers still in queue."""
        results = []
        node = self.queue.head
        while node:
            results.append(node.value)
            node = node.next
        return results
