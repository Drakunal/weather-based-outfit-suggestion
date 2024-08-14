import sys
import os
import unittest
# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))
from mock import patch
from outfit_recommender import recommend_outfit

class TestOutfitRecommender(unittest.TestCase):

    @patch('outfit_recommender.load_outfits')
    def test_recommend_outfit(self, mock_load_outfits):
        mock_load_outfits.return_value = {
            'cold': 'Heavy coat, gloves, and scarf',
            'cool': 'Light jacket and jeans',
            'warm': 'T-shirt and shorts',
            'hot': 'Tank top and shorts'
        }

        self.assertEqual(recommend_outfit(5, 'snowy'), "Heavy coat, gloves, and scarf")
        self.assertEqual(recommend_outfit(15, 'cloudy'), "Light jacket and jeans")
        self.assertEqual(recommend_outfit(25, 'sunny'), "T-shirt and shorts")
        self.assertEqual(recommend_outfit(35, 'hot'), "Tank top and shorts")

if __name__ == '__main__':
    unittest.main()
