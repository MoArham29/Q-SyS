
from customer import Customer
from QStructure import Queue
from storage import load_data, save_data


class QueueSystem:
    def __init__(self):
        customers_list, customers_dict = load_data()

        self.queue = Queue()
        for c in customers_list:
            self.queue.enqueue(c)

        self.customers_by_ticket = customers_dict


    def register_customer(self, name, reason):
        customer = Customer(name, reason)
        self.queue.enqueue(customer)
        self.customers_by_ticket[customer.ticket] = customer

        save_data(self.list_waiting(), self.customers_by_ticket)
        return customer


    def call_next(self):
        next_customer = self.queue.dequeue()

        if next_customer:
            save_data(self.list_waiting(), self.customers_by_ticket, next_customer.ticket)
            return next_customer

        save_data(self.list_waiting(), self.customers_by_ticket, None)
        return None



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
