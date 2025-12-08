
from system import QueueSystem

def print_waiting_list(system: QueueSystem):
    waiting = system.list_waiting()
    if not waiting:
        print("\nNo customers currently waiting.")
        return

    print("\nWaiting customers:")
    for customer in waiting:
        print(f" - {customer}")

def main():
    system = QueueSystem()

    while True:
        print("\n=== Operator Dashboard ===")
        print("1. Call next customer")
        print("2. View waiting customers")
        print("3. Search by ticket number")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            next_customer = system.call_next()
            if next_customer:
                print(f"\nNow serving: {next_customer}")
            else:
                print("\nNo customers waiting in the queue.")

        elif choice == "2":
            print_waiting_list(system)

        elif choice == "3":
            ticket_input = input("Enter ticket number: ").strip()
            if not ticket_input.isdigit():
                print("Ticket number must be a positive integer.")
                continue

            ticket = int(ticket_input)
            customer = system.search_by_ticket(ticket)

            if customer:
                print(f"\nCustomer found: {customer}")
            else:
                print("\nNo customer found with that ticket number.")

        elif choice == "4":
            print("Exiting operator dashboard.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
