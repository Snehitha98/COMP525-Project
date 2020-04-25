"""
carlo.py
Contains methods that will process the air_bnb dataset
Carlo Capuz
Created 4/18/2020
Updated 4/24/2020
"""

# import mean - to use the mean()
from statistics import mean

class NYCAirbnbListings():
    """
    Contains functions that transforms data from the Airbnb dataset.
    """

    @classmethod
    def total_listings_in_neighborhood_group(cls, filename):
        """
        The function takes in a csv file and counts how many Airbnb listings
            are in each neighborhood group
        Input: filename (csv file)
        Returns: Dictionary
        keys: Neighborhood group name (string)
            values: total listings (integer)
        """

    @classmethod
    def average_neighborhood_info(cls, filename):
        """
        The function calculates the average price, average number of reviews,
            and average availability per year of the listings of each
            neighborhood
        Input: filename - csv file that contains the Airbnb listings
            information
        Returns: Dictionary
            keys (string) - neighborhood
            values (integer) - average price of the neighborhood
        """

def main():
    """
    Contains testing cases for the two methods of NYCAirbnbListings() class
    """
    # csv file that contains 10 entries
    filename_10 = 'air_bnb_10_data.csv'
    # csv file that contains 25 entries
    filename_25 = 'air_bnb_25_data.csv'

    # Testing cases for total_listings_in_neighborhood_group()
    result_total_10 = NYCAirbnbListings.total_listings_in_neighborhood_group(filename_10)
    result_total_25 = NYCAirbnbListings.total_listings_in_neighborhood_group(filename_25)
    # Output will say how many listings there are in Brooklyn
    print('There are ' + str(result_total_10['Brooklyn']) + ' Airbnb listings in Brooklyn.')
    # Output will say how many listings there are in each neighborhood groups
    print(str(result_total_25) + '\n')

if __name__ == '__main__':
    main()
