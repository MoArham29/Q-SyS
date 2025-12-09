import json
import os
from customer import Customer

DATA_FILE = "queue_data.json"


def load_data():
    """Load queue system data from JSON file."""
    if not os.path.exists(DATA_FILE):
        Customer.NextTicket = 1
        return [], {}, None

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        customers_list = []
        customers_dict = {}

        for item in data.get("queue", []):
            c = Customer(
                item["name"],
                item["reason"],
                item.get("phone", ""),   # safe fallback
                item.get("email", "")    # safe fallback
            )
            c.ticket = item["ticket"]
            c.arrival = item["arrival"]   # stored timestamp (string)

            customers_list.append(c)
            customers_dict[c.ticket] = c

        # Update ticket counter
        if customers_list:
            Customer.NextTicket = max(c.ticket for c in customers_list) + 1
        else:
            Customer.NextTicket = 1

        now_serving = data.get("now_serving")

        return customers_list, customers_dict, now_serving

    except json.JSONDecodeError:
        print("Error: queue_data.json is corrupted. Resetting system.")
        Customer.NextTicket = 1
        return [], {}, None


def save_data(queue_list, customers_dict, now_serving):
    """Save queue system data into JSON file."""
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
