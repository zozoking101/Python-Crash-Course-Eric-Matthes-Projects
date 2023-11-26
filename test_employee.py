# test_employess.py

import unittest
from Employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """Create an employee instance for testing."""
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        """Test giving the default raise amount."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test giving a custom raise amount."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)
        
if __name__ == '__main__':
    unittest.main()