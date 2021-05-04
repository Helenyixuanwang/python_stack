class bankAccount:
# don't forget to add some default values for these parameters!
# your code here! (remember, this is where we specify the attributes for our class)
# don't worry about user info here; we'll involve the User class soon
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


savings = bankAccount(0.01,500)
checking= bankAccount(balance=100)


savings.deposit(100).deposit(100).deposit(200).withdraw(150).yield_interest().display_account_info()
checking.deposit(50).deposit(50).withdraw(5).withdraw(50).withdraw(50).withdraw(5).yield_interest().display_account_info()