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

        # ---------------- Call next customer ----------------
        if choice == "1":
            next_customer = system.call_next()
            if next_customer:
                print(f"\nNow serving ticket #{next_customer.ticket} ({next_customer.name})")
                print("An email notification has been sent to the customer.\n")
            else:
                print("\nNo customers waiting in the queue.")

        # ---------------- View waiting customers ----------------
        elif choice == "2":
            waiting = system.list_waiting()
            if not waiting:
                print("\nNo customers waiting.")
            else:
                print("\nWaiting customers:")
                for customer in waiting:
                    print(f" - Ticket #{customer.ticket}: {customer.name} ({customer.reason})")

        # ---------------- Search by ticket number ----------------
        elif choice == "3":
            ticket = input("Enter ticket number: ")

            if not ticket.isdigit():
                print("Ticket must be a number.\n")
                continue

            found = system.search_by_ticket(int(ticket))
            if found:
                print(f"\nCustomer found:")
                print(f" - Name: {found.name}")
                print(f" - Ticket: {found.ticket}")
                print(f" - Reason: {found.reason}")
                print(f" - Email: {found.email}")
                print(f" - Phone: {found.phone}")
            else:
                print("\nNo customer found with that ticket number.")

        # ---------------- Exit ----------------
        elif choice == "4":
            print("Exiting Operator Dashboard.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    operator_app()
