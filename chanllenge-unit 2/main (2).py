# Define the BankAccount class
class BankAccount:
    # Initialize the attributes with the constructor
    def __init__(self, account_number, account_holder_name, account_balance):
        # Use double underscores to make the attributes private
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    # Define a method to deposit money
    def deposit(self, amount):
        # Check if the amount is positive
        if amount > 0:
            # Add the amount to the account balance
            self.__account_balance += amount
            # Print a confirmation message
            print(f"Deposited {amount} to {self.__account_number}.")
        else:
            # Print an error message
            print("Invalid amount. Please enter a positive value.")

    # Define a method to withdraw money
    def withdraw(self, amount):
        # Check if the amount is positive and less than or equal to the account balance
        if amount > 0 and amount <= self.__account_balance:
            # Subtract the amount from the account balance
            self.__account_balance -= amount
            # Print a confirmation message
            print(f"Withdrew {amount} from {self.__account_number}.")
        else:
            # Print an error message
            print("Invalid amount. Please enter a positive value that is less than or equal to your account balance.")

    # Define a method to display the account balance
    def display_balance(self):
        # Print the account balance with formatting
        print(f"The balance of {self.__account_number} is {self.__account_balance:.2f}.")

# Create an instance of the BankAccount class with some initial values
my_account = BankAccount("123456789", "John Doe", 10000)

# Test the deposit method with some valid and invalid amounts
my_account.deposit(5000)
my_account.deposit(-1000)

# Test the withdraw method with some valid and invalid amounts
my_account.withdraw(3000)
my_account.withdraw(20000)

# Test the display_balance method
my_account.display_balance()

# Try to access the account balance directly from outside the class 
#(this should raise an error)
print(my_account.__account_balance)
