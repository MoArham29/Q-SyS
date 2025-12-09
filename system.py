from customer import Customer
from QStructure import Queue
from storage import load_data, save_data
from notifications import notify_customer, send_sms


class QueueSystem:
    def __init__(self):
        customers_list, customers_dict, now_serving = load_data()

        self.queue = Queue()
        for c in customers_list:
            self.queue.enqueue(c)

        self.customers_by_ticket = customers_dict
        self.now_serving = now_serving


    def register_customer(self, name, reason, phone, email):
        """Create and enqueue a new customer with full contact details."""
        customer = Customer(name, reason, phone, email)

        self.queue.enqueue(customer)
        self.customers_by_ticket[customer.ticket] = customer

        # Save updated data
        save_data(self.list_waiting(), self.customers_by_ticket, self.now_serving)

        # Send SMS + Email confirmation
        notify_customer(customer.email, customer.phone, customer.ticket)

        return customer


    def call_next(self):
        """Serve the next customer and notify them by SMS."""
        next_customer = self.queue.dequeue()

        if next_customer:
            self.now_serving = next_customer.ticket
            save_data(self.list_waiting(), self.customers_by_ticket, self.now_serving)

            # SMS alert
            send_sms(
                next_customer.phone,
                f"Your number {next_customer.ticket} is now being served."
            )

            return next_customer

        else:
            self.now_serving = None
            save_data(self.list_waiting(), self.customers_by_ticket, self.now_serving)
            return None


    def search_by_ticket(self, ticket_number):
        return self.customers_by_ticket.get(ticket_number)


    def list_waiting(self):
        """Return list of customers still in queue."""
        results = []
        node = self.queue.head
        while node:
            results.append(node.value)
            node = node.next
        return results
