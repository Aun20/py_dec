'''
Regular methods: they have direct relationship with the object.
Class methods: they do not have direct relationship with the object but only with class
Static method: when there is no direct relation with either class or object
Especial method: 
'''

class Emp:

	raise_amt = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay): # when self is first argument, it means its taking instance variable as its first argument by default and such methods are called regular methods.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Emp.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def name_email(self):
		return f"{self.first} {self.last} {self.email}"

	def apply_raise(self):
		#self.pay = int(float(self.pay) * 1.04) - initially to assign rate manually everytime, later rate is assigned in the start on line no. 
		self.pay = int(float(self.pay) * self.raise_amt)

	@classmethod # when there is no relation with the object but with the class
	def set_raise_amt(cls, amount):
		#Emp.raise_amt = amount
		cls.raise_amt = amount # to use a class method, instead of changing details in class everytime

	@classmethod # can clso be used as additional constructors
	def from_str(cls, emp_str):
		first, last, pay = emp_1_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False

			return True

	def __repr__(self): # its used by developer. this method is meant for developers, because by calling this method they can come to know how an object is created.
		return f"Emp('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.fullname()} - {self.email}"

emp_1 = Emp('John', 'Mark', 50000)
emp_2 = Emp('Jane', 'K', 60000)
deeb_1 = Emp('D', 'A', 70000)

emp_1_str = 'John-Mark-50000' # if data is in the form of string

emp_1_str.split('-')
print(emp_1_str.split('-')) # this will return as 3 items which are recalled


emp_1_str.split('-')
first, last, pay = emp_1_str.split('-')
print(last)

new_emp_1 = Emp(first, last, pay) # we will change the values to first, last, pay since we have already assigned it in above lign

print(new_emp_1.pay)

new_emp_1 = Emp.from_str(emp_1_str)
print(new_emp_1.last)

# Emp.set_raise_amt(1.08)
# print(emp_1.raise_amt)

# print(deeb_1.email)
# print(emp_2.pay)


# print(emp_1.first+ ' ' +emp_1.last)
# print(f"{emp_1.first} {emp_1.last}")

# print(emp_2.fullname())
# print(emp_1.name_email()) # whenever you wanted to access any function, you have to add ()

# print(Emp.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.raise_amt)
# print(Emp.raise_amt)

# Emp.raise_amt = 2.00 # you can change the value anywhere under a class
# emp_2.raise_amt = 3.00 # this will change rasie amount for that particular employee

# print(emp_1.raise_amt)
# print(Emp.raise_amt)

# print(Emp.num_of_emps)

import datetime

#print(datetime.__file__)

my_date = datetime.date(2021,12,29)

print(Emp.is_workday(my_date))

print(deeb_1)

print(repr(emp_1))

'''
Subclassed : 