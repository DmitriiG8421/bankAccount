
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
    print("\n")
#Add a Deposit Method:
#Inside the class, define a deposit method that accepts an amount parameter.
#Check if the deposit amount is at least $10. If it is, add it to the balance and print a confirmation message. If it isn’t, print a message that the minimum deposit amount is $10.

    def deposit(self,amount):
            if amount>=10:

                self.balance += amount
                print(f"${amount} is deposited. {self.account_holder}'s new balance is ${self.balance}")
            else:
                print("Mininum balabne has to be $10. Try again!")
            
#Add a Withdrawal Method: 
#Define a withdraw method that accepts an amount parameter.
#Check if the amount is greater than zero and within the available balance. If both conditions are met, subtract it from the balance and print the updated balance. Otherwise, print a message indicating that the withdrawal is not possible.  

    def withdrwal(self, amount):
        if amount > 0 and amount <= self.balance:
            
            self.balance -= amount
            print(f'${amount} has been withdrawn.  {self.account_holder} new balance is ${self.balance}')
        else:
            print("Sorry, you cannot withdraw this amount. Try again!")


person1 = BankAccount("Mark", 100)
person1.deposit(300)

person2 = BankAccount("Alice")
person2.deposit(500)

print("\n")