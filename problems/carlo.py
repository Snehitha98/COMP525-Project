"""
carlo.py
Contains methods that will process the air_bnb dataset
Carlo Capuz
Created 4/18/2020
Updated 4/24/2020
"""

# import mean - to use the mean()
from statistics import mean
import csv

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
        # Output will be key - neighborhood group and value - total number of
        # listings in that neighborhood group
        total_listings = {}
        # Open and read the filename that's passed in the function. Set it as
        # data, so it's easier to call.
        # Include the encoding because Windows has an encoding error when
        # reading the whole dataset.
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
        # Write the output to a csv file
        f = open('output/total_listings.csv', 'w', newline='')
        writer = csv.writer(f)
        writer.writerow(['Neighborhood Group', 'Number of Listings'])
        for neighborhood_group, count in total_listings.items():
            writer.writerow([neighborhood_group, count])
        f.close()
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
        
        # Define and initialize accumulator
        # Initial value is an empty dictionary
        # Final output will be key - neighborhood
        # value - average price of listings for that neighborhood
        average_price = {}
        # Define and initialize an accumulator that will hold the list of
        # prices per neighborhood
        neighborhood_prices = {}
        # Open and read the filename that was passed in the function
        # pass in the encoding because Windows has an encoding error when
        # running the dataset. Set is as data so it will be easier to access.
        with open(filename, encoding="utf8") as data:
            # Iterate through each line of the filename, and start from the
            # second line. We will ignore the first line because that's the
            # header for the csv file.
            for line in data.readlines()[1:]:
                # We will split the line by commas, so we can access each
                # element. Splitting turns it into a list of words.
                splitted_data = line.split(',')
                # Access the element corresponding to neighborhood.
                neighborhood = splitted_data[5]
                # Access the element corresponding to price.
                price = splitted_data[9]
                # Construct the temporary dictionary
                # Check to see if neighborhood is not in the dictionary.
                if neighborhood not in neighborhood_prices:
                    # If it's not yet in the dictionary, initialize the key 
                    # (neighborhood) with a value of empty list.
                    neighborhood_prices[neighborhood] = []
                # Append the price to its key's value
                # Convert the price to int
                neighborhood_prices[neighborhood].append(int(price))
            # Iterate through the keys and values of the temporary dictionary
            # Use items(), so we can access the keys and values.
            for neighborhood, price in neighborhood_prices.items():
                # Create a variable that will hold the average of the prices
                # Use the mean() from statistics to get the average of the list
                average = mean(price)
                # Construct the accumulator
                # Set the key as the neighborhood, and its value - the average
                # price of the list.
                # round the price to 2 decimal places using round()
                average_price[neighborhood] = round(average, 2)
        # Write to a csv file
        f = open('output/average_price.csv', 'w', newline='')
        writer = csv.writer(f)
        writer.writerow(['Neighborhood', 'Average Price'])
        for neighborhood, average in average_price.items():
            writer.writerow([neighborhood, average])
        f.close()
        # return the accumulator average_price
        return average_price


def main():
    """
    Contains testing cases for the two methods of NYCAirbnbListings() class
    """
    # csv file that contains 1 entry
    filename_1 = 'data/air_bnb_1_data.csv'
    # csv file that contains 25 entries
    filename_25 = 'data/air_bnb_25_data.csv'
    # csv file that contains the whole data
    filename = 'data/air_bnb.csv'

    # total_listings_in_neighborhood_group()
    # Calls for total_listings_in_neighborhood_group()
    result_total_1 = NYCAirbnbListings.total_listings_in_neighborhood_group(filename_1)
    result_total_25 = NYCAirbnbListings.total_listings_in_neighborhood_group(filename_25)
    result_total = NYCAirbnbListings.total_listings_in_neighborhood_group(filename)

    # Output will say how many listings there are in each neighborhood groups
    print('Testing cases for total_listings_in_neighborhood_group()')
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
    print('\nTesting cases for average_neighborhood_price()')
    print('Testing 1 entry of data')
    print(result_price_1)
    print('\nTesting 25 entries of data')
    print(result_price_25)
    print('\nTesting the whole data')
    print(result_price)
    
if __name__ == '__main__':
    main()
