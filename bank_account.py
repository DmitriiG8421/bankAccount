
#Begin by creating a BankAccount class. This class will handle the account holder's name, balance, deposits, and withdrawals.
#Set up the Constructor:
#Inside the BankAccount class, define an __init__ method. This constructor should accept two parameters:
#account_holder: The name of the person who holds the account.
#balance: The starting balance (default should be set to zero).
#Use self to assign these parameters to instance variables self.account_holder and self.balance


class BankAccount:
    
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
            if amount>=10:

                self.balance += amount
                print(f"${amount} is deposited. Your new balance is ${self.balance}")
            else:
                print("Mininum balance has to be $10. Try again!")
            
    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            
            self.balance -= amount
            print(f'${amount} has been withdrawn. Your new balance is ${self.balance}')
        else:
            print("Sorry, you cannot withdraw this amount. Try again!")

    def checkBalance(self):
        print("Your balance is: ", self.balance)

accounts = {
    "alice":{"pin":1001},
    "bob":{"pin":1002},
    "john":{"pin":1003},
    "sam":{"pin":1004}
    }

def login():
    while True:
        user_name = input("Type your username: ")
        if user_name not in accounts:
            print("Username is not found. Try again!\n")
            continue
        pin_code = input("\nType you pin code: ")
        if pin_code != accounts[user_name]["pin"]:
            print("Pin code not found. Try again!\n")
            continue
        print("Welcome to your account,", user_name.capitalize)
        user_name = BankAccount(user_name.capitalize)