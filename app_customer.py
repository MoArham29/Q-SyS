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
            phone = input("Enter your phone number (optional): ")
            email = input("Enter your email (required): ")

            if not name.strip():
                print("\nName is required.\n")
                continue

            if not email.strip():
                print("\nEmail is required.\n")
                continue

            customer = system.register_customer(name, reason, phone, email)

            print("\nRegistration Successful!")
            print(f"Your ticket number is: {customer.ticket}")
            print(f"A confirmation email has been sent to {email}.\n")

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    customer_app()
