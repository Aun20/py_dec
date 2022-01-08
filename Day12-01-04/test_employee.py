import unittest
from employee import Emp

class TestEmp(unittest.Testcase):

	def setup(self):
		self.emp_1 = Emp('John', 'Mark', 50000)
		self.emp_2 = Emp('Jane', 'K', 60000)

	def test_email(self):

		#emp_1 = Emp('John', 'Mark', 50000) - no need to assign value again and again as it is already assigned in line 7 & 8
		#emp_2 = Emp('Jane', 'K', 60000)

		self.assertEqual(self.emp_1.email, 'John.Mark@company.com')
		self.assertEqual(self.emp_2.email, 'Jane.K@company.com')

		self.emp_1.first = 'Kate' # we are using self. infront of all emp_ since it is assigned above
		self.emp_1.first = 'Tom'

		self.assertEqual(self.emp_1.email, 'Kate.Mark@company.com')
		self.assertEqual(self.emp_2.email, 'Tom.K@company.com')


	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'John Mark')
		self.assertEqual(self.emp_2.fullname, 'Jane K')

		self.emp_1.first = 'Kate'
		self.emp_1.first = 'Tom'

		self.assertEqual(self.emp_1.fullname, 'Kate Mark')
		self.assertEqual(self.emp_2.fullname, 'Tom K')


	def test_apply_raise(self):

		self.assertEqual(self.emp_1.fullname, 'John Mark')
		self.assertEqual(self.emp_2.fullname, 'Jane K')

		self.emp_1.first = 'Kate'
		self.emp_1.first = 'Tom'

		self.assertEqual(self.emp_1.fullname, 'Kate Mark')
		self.assertEqual(self.emp_2.fullname, 'Tom K')

if __name__ == '__main__':
	unittest.main()
