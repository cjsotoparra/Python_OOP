class Bankaccount:

	def __init__(self):
		self.balance = 0

	def get_balance(self):
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			print("Not Enough Funds")
		else:
			self.balance = self.balance-amount
			return self.balance

	def deposit(self, amount):
		self.balance = self.balance+amount

class Checking(Bankaccount):

	def __init__(self):
		Bankaccount.__init__(self)
		self.fee = 1.99

	def transfer(self, amount):
		if amount + self.fee > self.balance:
			print("Not Enough Funds")
		else:
			self.balance = self.balance- amount - self.fee
