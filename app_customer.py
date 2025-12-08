


from system import QueueSystem

def main():
    system = QueueSystem()

    while True:
        print("\n=== Customer Check-In ===")
        print("1. Register")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter your name: ").strip()
            reason = input("Reason for visit: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            if not reason:
                print("Reason cannot be empty.")
                continue

            customer = system.register_customer(name, reason)

            print("\nThank you for registering!")
            print(f"Your ticket number is: {customer.ticket}")
            print("Please wait until your number is called.\n")

        elif choice == "2":
            print("Goodbye.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
