import json
import os
from customer import Customer

DATA_FILE = "queue_data.json"


def load_data():
    """Load queue system data from JSON."""
    if not os.path.exists(DATA_FILE):
        return [], {}, None  # empty queue, empty dict, now_serving None

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        customers_list = []
        customers_dict = {}

        for item in data.get("queue", []):
            c = Customer(
                item["name"],
                item["reason"],
                item["phone"],
                item["email"]
            )
            c.ticket = item["ticket"]              # Override auto-ticketing
            c.arrival = item["arrival"]            # stored timestamp string
            customers_list.append(c)
            customers_dict[c.ticket] = c

        # Update NextTicket to match last used ticket +1
        if customers_list:
            Customer.NextTicket = max(c.ticket for c in customers_list) + 1

        now_serving = data.get("now_serving", None)

        return customers_list, customers_dict, now_serving

    except json.JSONDecodeError:
        print("Corrupted JSON file. Starting fresh.")
        return [], {}, None


def save_data(queue_list, customers_dict, now_serving):
    """Save queue system data to JSON."""
    data = {
        "queue": [
            {
                "ticket": c.ticket,
                "name": c.name,
                "reason": c.reason,
                "phone": c.phone,
                "email": c.email,
                "arrival": str(c.arrival)
            }
            for c in queue_list
        ],
        "now_serving": now_serving
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
