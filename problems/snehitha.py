"""
snehitha.py
Contains methods that will process the air_bnb dataset
Snehitha Mamidi
Created date : 4/18/2020
"""


class NYCAirbnbListings():
    """
    Contains functions that transforms data from the Airbnb dataset.
    """

    @classmethod
    def highest_reviewed_listing(cls, filename):
        """
        The function produces the listings details of name, price,neighborhood
        which has highest number of reviews of that neighborhood group.
        Input : filename that has the name of the csv file which
                contains Airbnb listings.
        Returns Dictionary
           keys : string - neighborhood group
           values : list - name, price, neighborhood of that neighborhood group
        """

    @classmethod
    def average_price_by_room_type(cls, filename):
        """
        Calculates the average price of room type of each neighborhood group.
        Input : filename that has the name of the csv file which
                contains Airbnb listings.
        Returns Dictionary
           keys : string – room type
           values : Dictionary
                     keys : string – neighborhood group
                     values : integer – average price
        """


def main():
    """
    Contains testing cases for the two methods of NYCAirbnbListings() class
    """

    # testing cases for highest_reviewed_listing()

    # test case 1 with whole dataset
    filename = 'air_bnb.csv'
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    print(f'highest reviewed listing in {filename} returns {actual_result}')
    # test case 2 with one entry
    filename = 'listing1.csv'
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    print(f'highest reviewed listing in {filename} returns {actual_result}')
    # test case 3 with five entries
    filename = 'listing2.csv'
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    print(f'highest reviewed listing in {filename} returns {actual_result}')
    # test case 4 to print info of heighest reviewed listing in Manhattan
    filename = 'air_bnb.csv'
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    result = actual_result['Manhattan']
    print(f'highest reviewed info for Manhattan returns {result}')

    # testing cases for average_price_by_room_type()

    # test case 1 with whole dataset
    filename = 'air_bnb.csv'
    actual_result = NYCAirbnbListings.average_price_by_room_type(filename)
    print(f'average price by room type in {filename} returns {actual_result}')
    # test case 2 with one entry
    filename = 'avgprice1.csv'
    actual_result = NYCAirbnbListings.average_price_by_room_type(filename)
    print(f'average price by room type in {filename} returns {actual_result}')
    # test case 3 with five entries
    filename = 'avgprice2.csv'
    actual_result = NYCAirbnbListings.average_price_by_room_type(filename)
    print(f'average price by room type in {filename} returns {actual_result}')
    # test case 4 to display the average price of Private room in each
    # neighborhood group
    filename = 'air_bnb.csv'
    actual_result = NYCAirbnbListings.average_price_by_room_type(filename)
    result = actual_result['Private room']
    print(f'average price of Private room returns {actual_result}')


if __name__ == '__main__':
    main()
