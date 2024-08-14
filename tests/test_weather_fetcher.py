import sys
import os
import unittest
# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))
from weather_fetcher import get_weather

class TestWeatherFetcher(unittest.TestCase):
    def test_get_weather(self):
        # Call the function
        temp, description = get_weather()

        # Basic checks
        self.assertIsInstance(temp, (int, float), "Temperature should be a number")
        self.assertIsInstance(description, str, "Weather description should be a string")

        # Further checks can be added if needed

if __name__ == '__main__':
    unittest.main()
