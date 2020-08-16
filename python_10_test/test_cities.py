import unittest
from city_functions import city_functions


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_functions('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago,Chile')

    def test_city_country_population(self):
        formatted_city = city_functions('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago,Chile - population 5000000')


unittest.main()
