class Emp:

	def __init__(self, first, last, pay): # there should be double underscore in init method for it to run
		self.first = first
		self.last = last
		self.pay = pay
		#self.email = first + '.' + last + '@company.com'

	@property # this decorator is added to a method so that you do not have to use parenthesis
	def email(self):
		return f"{self.first}.{self.last}@company.com"

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

emp_1 = Emp('John', 'Mark', 50000)

emp_1.first = 'Kate'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname) # wherever method is used it is used by parenthesis but not always




