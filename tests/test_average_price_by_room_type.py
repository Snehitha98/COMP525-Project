"""
test_average_price_by_room_type.py
Test cases to verify test_average_price_by_room_type.py
Snehitha Mamidi
created date: 04/29/2020
updated date: 05/06/2020
"""
import unittest
from problems.snehitha import NYCAirbnbListings


class TestAveragePriceByRoomType(unittest.TestCase):
    """
    Tests for average_price_by_room_type method
    """

    def test_one_entry(self):
        """
        Test method for average_price_by_room_type with input file
        avgprice1.csv
        """
        test_case = NYCAirbnbListings()
        filename = 'data/avgprice1.csv'
        actual_result = test_case.average_price_by_room_type(filename)
        expected_result = {'"Private room"': 149}
        self.assertDictEqual(actual_result, expected_result)

    def test_five_entries(self):
        """
        Test method for average_price_by_room_type with input file
        avgprice2.csv"
        """
        test_case = NYCAirbnbListings()
        filename = 'data/avgprice2.csv'
        actual_result = test_case.average_price_by_room_type(filename)
        expected_result = {
            '"Private room"': 149.5,
            '"Entire home/apt"': 131.33
        }
        self.assertDictEqual(actual_result, expected_result)

    def test_multiple_entries(self):
        """
        Test method for average_price_by_room_type with input file
        air_bnb.csv
        """
        test_case = NYCAirbnbListings()
        filename = 'data/air_bnb.csv'
        actual_result = test_case.average_price_by_room_type(filename)
        expected_result = {
            '"Private room"': 89.78,
            '"Entire home/apt"': 211.79,
            '"Shared room"': 70.13
        }
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
