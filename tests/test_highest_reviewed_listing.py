"""
test_highest_reviewed_listing.py
Test cases to verify test_highest_reviewed_listing.py
Snehitha Mamidi
created date: 04/26/2020
"""
import unittest
from problems.snehitha import NYCAirbnbListings


class TestHighestReviewedListing(unittest.TestCase):
    """
    Tests for highest_reviewed_listing method
    """

    def test_one_entry(self):
        """
        Test method for highest_reviewed_listing with input file
        listing1.csv
        """
        test_case = NYCAirbnbListings()
        actual_result = test_case.highest_reviewed_listing('listing1.csv')
        expected_result = {
            '"Brooklyn"': ['"Clean & quiet apt home by the park"',
                           '149', '"Kensington"']
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_five_entries(self):
        """
        Test method for highest_reviewed_listing with input file
        listing2.csv"
        """
        test_case = NYCAirbnbListings()
        actual_result = test_case.highest_reviewed_listing('listing2.csv')
        expected_result = {
            '"Manhattan"': ['"Skylit Midtown Castle"', '225', '"Midtown"'],
            '"Brooklyn"': ['"Cozy Entire Floor of Brownstone"',
                           '89', '"Clinton Hill"']
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_multiple_entries(self):
        """
        Test method for highest_reviewed_listing with input file
        air_bnb.csv
        """
        test_case = NYCAirbnbListings()
        actual_result = test_case.highest_reviewed_listing('air_bnb.csv')
        expected_result = {
            '"Staten Island"': ['"D Private Che@p Room 2 Explore NYC"',
                                '36', '"Tompkinsville"'],
            '"Manhattan"': ['"Great Bedroom in Manhattan"', '49', '"Harlem"'],
            '"Brooklyn"': ['"Private brownstone studio Brooklyn"',
                           '160', '"Park Slope"'],
            '"Bronx"': ['"Cozy Private Bedroom"', '53', '"Mott Haven"'],
            '"Queens"': ['"Room near JFK Queen Bed"', '47', '"Jamaica"']
        }

        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
