class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000  # Initial balance for demonstration purposes

class ATM:
    def __init__(self):
        self.users = {}  # Dictionary to store user data
        self.current_user = None

    def create_user(self, user_id, pin):
        user = User(user_id, pin)
        self.users[user_id] = user

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            return True
        return False

    def deposit(self, amount):
        if self.current_user:
            self.current_user.balance += amount
            return f"Deposited ${amount}. New balance: ${self.current_user.balance}"

    def withdraw(self, amount):
        if self.current_user:
            if self.current_user.balance >= amount:
                self.current_user.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.current_user.balance}"
            else:
                return "Insufficient funds."

    def transfer(self, to_user_id, amount):
        if self.current_user:
            if to_user_id in self.users:
                if self.current_user.balance >= amount:
                    self.current_user.balance -= amount
                    self.users[to_user_id].balance += amount
                    return f"Transferred ${amount} to {to_user_id}. New balance: ${self.current_user.balance}"
                else:
                    return "Insufficient funds."
            else:
                return "Recipient user not found."

    def transaction_history(self):
        if self.current_user:
            return f"Transaction history for {self.current_user.user_id}: (Not implemented in this example)"

    def quit(self):
        self.current_user = None
        return "Logged out."

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Create User")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")
            atm.create_user(user_id, pin)
            print(f"User {user_id} created successfully.")

        elif choice == "2":
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")
            if atm.login(user_id, pin):
                print(f"Logged in as {user_id}.")
            else:
                print("Invalid User ID or PIN.")

        elif choice == "3":
            amount = float(input("Enter deposit amount: "))
            result = atm.deposit(amount)
            print(result)

        elif choice == "4":
            amount = float(input("Enter withdrawal amount: "))
            result = atm.withdraw(amount)
            print(result)

        elif choice == "5":
            to_user_id = input("Enter recipient User ID: ")
            amount = float(input("Enter transfer amount: "))
            result = atm.transfer(to_user_id, amount)
            print(result)

        elif choice == "6":
            history = atm.transaction_history()
            print(history)

        elif choice == "7":
            print(atm.quit())
            break

if __name__ == "__main__":
    main()
