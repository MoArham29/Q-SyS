from system import QueueSystem

def customer_app():
    system = QueueSystem()

    while True:
        print("\n=== Customer Check-In ===")
        print("1. Register")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            reason = input("Reason for visit: ")

            if not name.strip():
                print("Name is required.\n")
                continue
            if not reason.strip():
                print("Reason is required.\n")
                continue

            customer = system.register_customer(name, reason)

            print("\nRegistration Successful!")
            print(f"Your ticket number is: {customer.ticket}")
            print("Please wait until your number is called.\n")

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    customer_app()
