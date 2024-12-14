
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

    def deposit(self, amount):
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

    def logOut(self):
        youSure = input("Are you sure you want to log out. 'yes' to log out. 'no' you not log out\n")
        if youSure == "yes":
            print("You are logged out!")
            return True
        else:
            print("You are NOT logged out!")
            return False

accounts = {
    "alice":{"pin":1001},
    "bob":{"pin":1002},
    "john":{"pin":1003},
    "sam":{"pin":1004}
    }

while True:
    user_name = input("\nType your username: ")
    if user_name not in accounts:
        print("Username is not found. Try again")
        continue
    pin_code = int(input("\nType your pin code: "))
    if pin_code!=accounts[user_name]["pin"]:
        print("Pincode not found. Try again!")
        continue
    print("\nWelcome to your account,",user_name.capitalize())
    user_account = BankAccount(user_name.capitalize())

    while True:
        option = input("Which option do you choose?\n Type '1' for deposit\n Type '2' for withdrawal\n Type '3' to check balance\n Type '4' to log out\nOption: ")
        
        if option == "1":
            user_account.deposit(int(input("How much would you like to deposit: ")))

        if option == "2":
            user_account.withdrawal(int(input("How much would you like to withdraw: ")))

        if option == "3":
            user_account.checkBalance()

        if option == "4":
            isLoggedOut = user_account.logOut()
            if isLoggedOut:
                break
            

        print("\n")
        #test