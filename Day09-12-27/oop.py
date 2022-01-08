'''
Object-oriented programming (OOP) is a programming
paradigm based on the concept of "objects", which can contain
and code: data in the form of fields (often known as attributes or properties), and code in the form of procedures (often known as methods).

Class and Instances/Objects

class - is in which you group the data. It is common attribute which is shared among all.

# Emp - is class. # whenever you create a class define it in init method. Initializing the class, when you create functions inside a class its called a method.

'''

class Emp:

	raise_amt = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay): # there should be double underscore in init method for it to run
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

# emp_1.id = id # init function you assign the value
# emp_1.first = first
# emp_1.last = last
# emp_1.pay = pay
# emp_1.email = first + '.' + last + '@company.com'
# self - takes instance variable as its first argument, instead of changing emp_1 everytime for a new person.

emp_1 = Emp('John', 'Mark', 50000)
emp_2 = Emp('Jane', 'K', 60000)
deeb_1 = Emp('D', 'A', 70000)

# Example for employee at a company

# emp_1.id = 1
# emp_1.first_name = 'John'
# emp_1.last_name = 'Mark'
# emp_1.email = 'John.mark@company.com'

# emp_2.id = 2 # DRY - Dont repeat yourself. Instead of writing the same code over and over again we store data in a better way. And assign the details under a class.
# emp_2.first_name = 'Jane'
# emp_2.last_name = 'K'
# emp_2.email = 'John.mark@company.com'

print(deeb_1.email)
print(emp_2.pay)


print(emp_1.first+ ' ' +emp_1.last)
print(f"{emp_1.first} {emp_1.last}")

print(emp_2.fullname())
print(emp_1.name_email()) # whenever you wanted to access any function, you have to add ()

print(Emp.fullname(emp_2))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amt)
print(Emp.raise_amt)

Emp.raise_amt = 2.00 # you can change the value anywhere under a class
emp_2.raise_amt = 3.00 # this will change rasie amount for that particular employee

print(emp_1.raise_amt)
print(Emp.raise_amt)

print(Emp.num_of_emps)
