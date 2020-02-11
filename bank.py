

class Account:


	def __init__(self):

		self.balance=0


	def create_account(self):

		print(" ")

		print("Hello!Please give your account details")

		self.account_number=input("Enter account number:")
		self.account_name=input("Name of the account holder:")
		self.account_type=input("Type of account Please:")

		if self.account_type=="fixed deposit account":
			self.fd=input("please enter fixed deposit value:")

	
	def show_account(self):

		print(" ")

		print("Account number is",self.account_number)
		print(" ")
		print("Name of account holder is ",self.account_name)
		print(" ")
		print("Type of account is",self.account_type)

		if self.account_type=="current account":
			print("Balance in account is",self.balance)

		elif self.account_type=="fixed deposit account":

			print("Fixed deposit value is:",self.fd)

	def deposit(self):

		print(" ")

		if self.account_type=="fixed deposit account":
			print("soryy you have a fixed deposit account you cannot deposit")

		else:	


			d=input("how much money do you want to deposit:")

			self.balance+=int(d)

	def withdraw(self):

		print(" ")

		if self.account_type=="fixed deposit account":
			print("soryy you have a fixed deposit account you cannot withdraw")

		else:	

		
			c=input("How much money you want to withdraw:")

			if int(c)>self.balance:

				print("sorry you cannot withdraw")

			else:

				self.balance-=int(c)
				

	def show_account_number(self):

		print(" ")

		print("account number is",self.account_number)

	def	show_balance(self):

		print(" ")

		if self.account_type=="current account":



			print("Balance is",self.balance)

		else:

			print("Balance is",self.fd)
		



i=-1

accounts=[]
while True:

	print("What do you want to do:")
	print(" ")

	print("options: create_account  show_account  deposit  withdraw  show_account_number  show_balance")

	print(" ")
	data=input()

	if data=="create_account":

		i+=1

		a=Account()

		accounts.append(a)

		accounts[i].create_account()

		

	elif data=="show_account":
	
		accounts[i].show_account()


	elif data=="deposit":
	
		accounts[i].deposit()	

	elif data=="withdraw":

		accounts[i].withdraw()

	elif data=="show_account_number":
	
		accounts[i].show_account_number()

	elif data=="show_balance":
	
		accounts[i].show_balance()

	else:
	
		print("wrong input")	
		
