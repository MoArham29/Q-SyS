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
            phone = input("Enter your phone number (e.g. +447...): ")
            email = input("Enter your email: ")

            if not name.strip() or not reason.strip() or not phone.strip() or not email.strip():
                print("\nAll fields are required.\n")
                continue

            customer = system.register_customer(name, reason, phone, email)

            print("\nRegistration Successful!")
            print(f"Your ticket number is: {customer.ticket}")
            print("You will receive SMS + Email confirmation.\n")

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    customer_app()
