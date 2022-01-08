'''

Regular methods: they have direct relationship with the object.
Class methods: they do not have direct relationship with the object but only with class
Static method: when there is no direct relation with either class or object
Especial method: 
'''

class Emp:

	raise_amt = 1.04

	def __init__(self, first, last, pay): # when self is first argument, it means its taking instance variable as its first argument by default and such methods are called regular methods.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		#self.pay = int(float(self.pay) * 1.04) - initially to assign rate manually everytime, later rate is assigned in the start on line no. 
		self.pay = int(float(self.pay) * self.raise_amt)

class Dev(Emp):
	raise_amt = 1.23

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) # instead of writing all the details of a class mentioned before line (13-17)
		self.prog_lang = prog_lang


emp_1 = Dev('John', 'Mark', 50000, 'Python')
emp_2 = Emp('Jane', 'K', 60000)
deeb_1 = Emp('D', 'A', 70000)

print(emp_1.email)
print(emp_1.raise_amt)

print(emp_2.first)
print(emp_2.raise_amt)