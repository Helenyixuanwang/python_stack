class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

#make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

#display_user_balance(self) - have this method print the user's name and account balance to the terminal
#eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

#BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self,other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} Transfer money ${amount} to {other_user.name}")
        return self




grace = User("Grace", "grace@hotmail.com")
cathy = User("Cathy", "cathy@gmail.com")
brian = User("Brian","brian@yahoo.com")

#first user Grace, 3 dposits, 1 withdrawl and display balance
grace.make_deposit(100).make_deposit(123).make_deposit(350).make_withdrawal(99).display_user_balance()



#second user Cathy, 2 deposits, 2 withdrawls and display balance
cathy.make_deposit(200).make_deposit(288).make_withdrawal(33).make_withdrawal(66).display_user_balance()

#third user Brian, 1 deposit, 3 withdrawls and display balance
brian.make_deposit(1000).make_withdrawal(68).make_withdrawal(17).make_withdrawal(133).display_user_balance()


#transfer from grace to brian
grace.display_user_balance().transfer_money(brian, 23).display_user_balance()
#grace.transfer_money(brian, 23)
#grace.display_user_balance()
brian.display_user_balance()