import json
import os
from customer import Customer

DATA_FILE = "queue_data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return [], {}, None

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        customers_list = []
        customers_dict = {}

        for item in data.get("queue", []):
            c = Customer(item["name"], item["reason"])
            c.ticket = item["ticket"]
            customers_list.append(c)
            customers_dict[c.ticket] = c

        # Update next ticket
        if customers_list:
            Customer.NextTicket = max(c.ticket for c in customers_list) + 1

        return customers_list, customers_dict, data.get("now_serving")

    except json.JSONDecodeError:
        print("Error reading JSON, starting fresh.")
        return [], {}, None


def save_data(queue, customer_dict, now_serving=None):
    """Save queue system data to JSON."""
    data = {
        "queue": [
            {
                "ticket": c.ticket,
                "name": c.name,
                "reason": c.reason
            }
            for c in queue
        ],
        "now_serving": now_serving  
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
