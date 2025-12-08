from system import QueueSystem

def operator_app():
    system = QueueSystem()

    while True:
        print("\n=== Operator Dashboard ===")
        print("1. Call next customer")
        print("2. View waiting customers")
        print("3. Search by ticket number")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            next_customer = system.call_next()
            if next_customer:
                print(f"\nNow serving: {next_customer}")
            else:
                print("\nNo customers waiting in the queue.")

        elif choice == "2":
            waiting = system.list_waiting()
            if not waiting:
                print("\nNo customers waiting.")
            else:
                print("\nWaiting customers:")
                for customer in waiting:
                    print(f" - {customer}")

        elif choice == "3":
            ticket = input("Enter ticket number: ")

            if not ticket.isdigit():
                print("Ticket must be a number.\n")
                continue

            found = system.search_by_ticket(int(ticket))
            if found:
                print(f"\nCustomer found: {found}")
            else:
                print("\nNo customer found with that ticket number.")

        elif choice == "4":
            print("Exiting Operator Dashboard.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    operator_app()
