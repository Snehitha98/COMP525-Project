"""
test_total_listings_in_neighborhood_group.py
To test the total_listings_in_neighborhood_group()
Carlo Capuz
Created 4/25/2020
"""

import unittest
from problems.carlo import NYCAirbnbListings

class TestTotalListingsInNeighborhoodGroup(unittest.TestCase):
    """
    Contains test functions for total_listings_in_neighborhood_group()
    """

    def test_one_entry(self):
        """
        test 1 entry of data
        """

        nyc_airbnb_listing = NYCAirbnbListings()
        filename_1 = "data/air_bnb_1_data.csv"
        actual_result = nyc_airbnb_listing.total_listings_in_neighborhood_group(filename_1)
        expected_result = {'Manhattan': 1}
        self.assertDictEqual(actual_result, expected_result)

    def test_25_entry(self):
        """
        test 25 entries of data
        """

        nyc_airbnb_listing = NYCAirbnbListings()
        filename_25 = "data/air_bnb_25_data.csv"
        actual_result = nyc_airbnb_listing.total_listings_in_neighborhood_group(filename_25)
        expected_result = {'Brooklyn': 12, 'Manhattan': 13}
        self.assertDictEqual(actual_result, expected_result)

    def test_whole_data(self):
        """
        test whole data
        """

        nyc_airbnb_listing = NYCAirbnbListings()
        filename = "data/air_bnb.csv"
        actual_result = nyc_airbnb_listing.total_listings_in_neighborhood_group(filename)
        expected_result = {'"Brooklyn"': 20104, '"Manhattan"': 21661, '"Queens"': 5666,
                           '"Staten Island"': 373, '"Bronx"': 1091}
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
