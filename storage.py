import json
import os
from customer import customer

DATA_FILE = "queue_data.json"


def load_data():
    """Load queue system data from JSON."""
    if not os.path.exists(DATA_FILE):
        return [], {}

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        # Reconstruct Customer objects
        customers_list = []
        customers_dict = {}

        for item in data.get("queue", []):
            customer = customer(item["name"], item["reason"])
            customer.ticket = item["ticket"]   # override auto ticket
            customers_list.append(customer)
            customers_dict[customer.ticket] = customer

        # Update next ticket number
        if customers_list:
            customer._next_ticket = max(c.ticket for c in customers_list) + 1

        return customers_list, customers_dict

    except json.JSONDecodeError:
        print("Error reading JSON file. Starting fresh.")
        return [], {}


def save_data(queue, customer_dict):
    """Save queue system data to JSON."""
    data = {
        "queue": [
            {
                "ticket": c.ticket,
                "name": c.name,
                "reason": c.reason
            }
            for c in queue
        ]
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
