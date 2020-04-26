"""
carlo.py
Contains methods that will process the air_bnb dataset
Carlo Capuz
Created 4/18/2020
Updated 4/24/2020
"""

# import mean - to use the mean()
#from statistics import mean

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

        # Define and initialize our accumulator
        # Initial value is an empty dictionary
        total_listings = {}
        # Open and read the filename that's passed in the function. Set it as
        # data, so it's easier to call.
        with open(filename, encoding="utf8") as data:
            # Iterate through each line of the data.
            # Start the reading on the second line of the file. The first line
            # of the file is the header, so we need to skip it.
            for line in data.readlines()[1:]:
                # Split the line by commas, so we can access each element in
                # the data.
                splitted_data = line.split(',')
                # Get the neighborhood group by accessing the element
                neighborhood_group = splitted_data[4]
                # Construct the dictionary
                # Check to see if the key neighborhood_group is not in the
                # dictionary
                if neighborhood_group not in total_listings:
                    # If it's not in the dictionary, initialize the key's value
                    # by 1
                    total_listings[neighborhood_group] = 1
                else:
                    # If it's in the dictionary, increment its value by 1
                    total_listings[neighborhood_group] += 1
        # return the accumulator
        return total_listings


    @classmethod
    def average_neighborhood_price(cls, filename):
        """
        The function calculates the average price of the listings of each
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
    # csv file that contains 1 entry
    filename_1 = 'air_bnb_1_data.csv'
    # csv file that contains 25 entries
    filename_25 = 'air_bnb_25_data.csv'
    # csv file that contains the whole data
    filename = 'air_bnb.csv'

    # total_listings_in_neighborhood_group()
    # Calls for total_listings_in_neighborhood_group()
    result_total_1 = NYCAirbnbListings.total_listings_in_neighborhood_group(filename_1)
    result_total_25 = NYCAirbnbListings.total_listings_in_neighborhood_group(filename_25)
    result_total = NYCAirbnbListings.total_listings_in_neighborhood_group(filename)

    # Output will say how many listings there are in each neighborhood groups
    print('Testing 1 entry of data')
    print(result_total_1)
    print('\nTesting 25 entries of data')
    print(result_total_25)
    print('\nTesting the whole data')
    print(result_total)

    # average_neighborhood_price()
    result_price_1 = NYCAirbnbListings.average_neighborhood_price(filename_1)
    result_price_25 = NYCAirbnbListings.average_neighborhood_price(filename_25)
    result_price = NYCAirbnbListings.average_neighborhood_price(filename)

    # Output will display the average prices in each neighborhoods
    print('Testing 1 entry of data')
    print(result_price_1)
    print('\nTesting 25 entries of data')
    print(result_price_25)
    print('\nTesting the whole data')
    print(result_price)

if __name__ == '__main__':
    main()
