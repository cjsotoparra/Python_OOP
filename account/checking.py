from bankaccount import *

class Checking(Bankaccount):

	def transfer(self):
		print("tranfer something")


checking = Checking():
