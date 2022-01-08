class Emp:

	raise_amt = 1.08

	def __init__(self, first, last, pay): # there should be double underscore in init method for it to run
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	@property # this decorator is added to a method so that you do not have to use parenthesis
	def email(self):
		return f"{self.first}.{self.last}@company.com"

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		#self.pay = int(float(self.pay) * 1.04) - initially to assign rate manually everytime, later rate is assigned in the start on line no. 
		self.pay = int(float(self.pay) * self.raise_amt)


emp_1 = Emp('John', 'Mark', 50000)
emp_2 = Emp('Jane', 'K', 60000)

emp_1.apply_raise()
print(emp_1.pay)





