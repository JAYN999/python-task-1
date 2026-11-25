import time

DEMO_PIN = "2005"
INITIAL_BALANCE = 78000
MAX_PIN_ATTEMPTS = 3


def read_amount(prompt):
    """Read a positive whole-number amount; return None for invalid input."""
    try:
        amount = int(input(prompt).strip())
    except ValueError:
        print("Please enter a valid whole number.")
        return None

    if amount <= 0:
        print("Amount must be greater than zero.")
        return None

    return amount


def main():
    balance = INITIAL_BALANCE

    print("PLEASE INSERT YOUR CARD")
    time.sleep(2)

    authenticated = False
    for attempt in range(MAX_PIN_ATTEMPTS):
        pin = input("ENTER YOUR ATM PIN: ").strip()
        if pin == DEMO_PIN:
            authenticated = True
            print("PIN accepted.")
            break

        attempts_left = MAX_PIN_ATTEMPTS - attempt - 1
        if attempts_left:
            print(f"Wrong PIN. You have {attempts_left} attempt(s) left.")
        else:
            print("Too many incorrect attempts. Transaction cancelled.")

    if not authenticated:
        return

    while True:
        print(
            """
            1 == Balance enquiry
            2 == Withdraw money
            3 == Deposit money
            4 == Exit
            """
        )

        try:
            option = int(input("PLEASE ENTER YOUR CHOICE: ").strip())
        except ValueError:
            print("Please enter a valid menu option (1-4).")
            continue

        if option == 1:
            print(f"YOUR CURRENT BALANCE IS Rs. {balance}")

        elif option == 2:
            amount = read_amount("PLEASE ENTER YOUR WITHDRAWAL AMOUNT: ")
            if amount is None:
                continue
            if amount > balance:
                print("Insufficient balance. Withdrawal cancelled.")
                continue

            balance -= amount
            print(f"Rs. {amount} has been debited from your account.")
            print(f"YOUR UPDATED BALANCE IS Rs. {balance}")

        elif option == 3:
            amount = read_amount("PLEASE ENTER YOUR DEPOSIT AMOUNT: ")
            if amount is None:
                continue

            balance += amount
            print(f"Rs. {amount} has been credited to your account.")
            print(f"YOUR UPDATED BALANCE IS Rs. {balance}")

        elif option == 4:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 4.")


if __name__ == "__main__":
    main()
