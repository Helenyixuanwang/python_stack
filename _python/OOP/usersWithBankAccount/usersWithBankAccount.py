#Make sure that by the end of this assignment that you:

#have both the User and BankAccount classes in the same file for your assignment
#only create BankAccount instances inside of the User's __init__ method
#only call BankAccount methods inside of the methods in the User class


class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankAccount(int_rate=0.01)
    
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        return self


    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self


    def display_user_balance(self):
        self.account.display_account_info()
        return self


    def transfer_money(self,other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        print(f"{self.name} Transfer money ${amount} to {other_user.name}")
        return self
        
class bankAccount:
#
    def __init__(self, int_rate=0.00, balance=0): 
        self.rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

#decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self    


# print to the console: eg. "Balance: $100"		
    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self
		
 #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.rate*self.account_balance
            
        else:
            print("Bank account is negative. No interest")
        return self       



grace = User("Grace", "grace@hotmail.com")
cathy = User("Cathy", "cathy@gmail.com")
brian = User("Brian","brian@yahoo.com")

#first user Grace, 3 dposits, 1 withdrawl and display balance
grace.make_deposit(100).make_deposit(50).make_deposit(50).make_withdrawal(100).display_user_balance()



#second user Cathy, 2 deposits, 2 withdrawls and display balance
cathy.make_deposit(200).make_deposit(200).make_withdrawal(300).make_withdrawal(50).display_user_balance()

#third user Brian, 1 deposit, 3 withdrawls and display balance
brian.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()


#transfer from grace to brian
grace.display_user_balance().transfer_money(brian, 10).display_user_balance()
brian.display_user_balance()