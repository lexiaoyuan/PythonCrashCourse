import unittest
from employee import Employee


class TestEmplyee(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('xiaoyuan', 'le', 8000)

    def test_give_default_raise(self):
        my_raise = self.my_employee.give_raise()
        self.assertEqual(my_raise, 5000)

    def test_give_custom_raise(self):
        my_raise = self.my_employee.give_raise(8000)
        self.assertEqual(my_raise, 8000)


unittest.main()
