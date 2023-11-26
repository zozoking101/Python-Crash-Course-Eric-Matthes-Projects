# test_cities_population.py

import unittest
from Population import get_formatted_city

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'Population.py'."""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city_country = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - population 5000000' work?"""
        formatted_city_country = get_formatted_city('santiago', 'chile', population=5000000)
        self.assertEqual(formatted_city_country, 'Santiago, Chile – population 5000000')
        
if __name__ == '__main__':
    unittest.main()