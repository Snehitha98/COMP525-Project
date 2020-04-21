"""
carlo.py
Contains methods that will process the air_bnb dataset
Carlo Capuz
Created 4/18/2020
"""

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
        return None

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
            values (integer) - average number of reviews, price,
                and availability of listings in that neighborhood
        """
        return None

def main():
    """
    Contains testing cases for the two methods of NYCAirbnbListings() class
    """

    filename = 'air_bnb.csv'

    # Testing cases for total_listings_in_neighborhood_group()
    result_total = NYCAirbnbListings.total_listings_in_neighborhood_group(filename)
    # Output will say how many listings there are in Brooklyn
    print(result_total['Brooklyn'])
    # Output will say how many listings there are in each neighborhood
    # groups
    print(result_total)

    # Testing cases for total_listings_in_neighborhood_group()
    result_info = NYCAirbnbListings.average_neighborhood_info(filename)
    # Output will display average price, average number of reviews and
    # average availability of this neighborhood.
    print(result_info['Kensington'])
    # This will display all the neighborhoods' average price, number of
    # reviews and availability
    print(result_info)

if __name__ == '__main__':
    main()
