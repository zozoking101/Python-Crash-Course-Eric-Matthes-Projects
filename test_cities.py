# test_cities.py

import unittest
from City_Country import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does the function return the correct string?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()