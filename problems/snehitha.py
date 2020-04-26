"""
snehitha.py
Contains methods that will process the air_bnb dataset
Snehitha Mamidi
Created date : 4/18/2020
updated date : 4/26/2020
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
        file_ref = open(filename, 'r')
        list_of_reviews_d = {}
        for line in file_ref.readlines()[1:]:
            line_row = line.split(',')
            neighborhood_grp = line_row[4]
            reviews = line_row[11]
            if neighborhood_grp in list_of_reviews_d:
                list_of_reviews_d[neighborhood_grp].append(reviews)
            else:
                list_of_reviews_d[neighborhood_grp] = [reviews]
        file_ref.close()
        highest_review_d = {}
        for neighborhood_grp in list_of_reviews_d:
            str_to_int = list(map(int, list_of_reviews_d[neighborhood_grp]))
            highest_review_d[neighborhood_grp] = max(str_to_int)
        result_d = {}
        file_ref = open(filename, 'r')
        for line in file_ref.readlines()[1:]:
            line_row = line.split(',')
            name = line_row[1]
            neighborhood_grp = line_row[4]
            neighborhood = line_row[5]
            price = line_row[9]
            reviews = line_row[11]
            for key in highest_review_d:
                if reviews == str(highest_review_d[key]):
                    if neighborhood_grp == key:
                        result_d[key] = [name] + [price] + [neighborhood]
        file_ref.close()
        return result_d

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
    # test case 1 with one entry
    print('****Test case:1****')
    filename = 'listing1.csv'
    expected_result = {
        '"Brooklyn"': ['"Clean & quiet apt home by the park"',
                       '149', '"Kensington"']
    }
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    print(f'highest reviewed listing in {filename}')
    print(f'Actual: {actual_result}')
    print(f'Expected: {expected_result}')
    # test case 2 with five entries
    print('\n****Test case:2****')
    filename = 'listing2.csv'
    expected_result = {
        '"Manhattan"': ['"Skylit Midtown Castle"', '225', '"Midtown"'],
        '"Brooklyn"': ['"Cozy Entire Floor of Brownstone"',
                       '89', '"Clinton Hill"']
    }
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    print(f'highest reviewed listing in {filename}')
    print(f'Actual: {actual_result}')
    print(f'Expected: {expected_result}')
    # test case 3 with whole dataset
    print('\n****Test case:3****')
    filename = 'air_bnb.csv'
    expected_result = {
        '"Staten Island"': ['"D Private Che@p Room 2 Explore NYC"',
                            '36', '"Tompkinsville"'],
        '"Manhattan"': ['"Great Bedroom in Manhattan"', '49', '"Harlem"'],
        '"Brooklyn"': ['"Private brownstone studio Brooklyn"',
                       '160', '"Park Slope"'],
        '"Bronx"': ['"Cozy Private Bedroom"', '53', '"Mott Haven"'],
        '"Queens"': ['"Room near JFK Queen Bed"', '47', '"Jamaica"']
    }
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    print(f'highest reviewed listing in {filename}')
    print(f'Actual: {actual_result}')
    print(f'Expected: {expected_result}')
    # test case 4 to print info of heighest reviewed listing in Manhattan
    print('\n****Test case:4****')
    filename = 'air_bnb.csv'
    expected_result = ['"Great Bedroom in Manhattan"', '49', '"Harlem"']
    actual_result = NYCAirbnbListings.highest_reviewed_listing(filename)
    actual_result = actual_result['"Manhattan"']
    print(f'highest reviewed listing for Manhattan in {filename}')
    print(f'Actual: {actual_result}')
    print(f'Expected: {expected_result}')

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
    # result = actual_result['Private room']
    # print(f'average price of Private room returns {actual_result}')


if __name__ == '__main__':
    main()
