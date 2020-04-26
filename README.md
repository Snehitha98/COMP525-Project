# total_listings_in_neighborhood_group()
```
def total_listings_in_neighborhood_group(cls, filename):
        """
        The function takes in a csv file and counts how many Airbnb listings
            are in each neighborhood group
        Input: filename (csv file)
        Returns: Dictionary
        keys: Neighborhood group name (string)
            values: total listings (integer)
        """
```
Accumulation Pattern
* We're going to use accumulation pattern to be able to get the data needed for
    our output.
* First, we need to declare and initialize our accumulator named
    **total_listings**.
     * Initial value of **total_listings** is an empty dictionary. We will
        populate our accumulator with data later on.
* Then, we're going to open and read **filename** that was passed in the 
    function.
    * Iterate through each line of the file by using readlines(). We're also
        going to start from the second line, since the first line is the header.
    * While iterating, we're going to split each line by commas.
        * This will turn each line into a list. This way we can access each
            element in the list.
        * We're going to get the data corresponding to the required information.
            * We need to access **neighborhood_group**, which is the 4th index.
        * Construct our dictionary (output)
            * Check to see if **neighborhood_group** is not in the dicitonary.
                * If it's not there, initialize its key and its value by 1.
                * If it is there, increment its value by 1.
* Return **total_listings**

# average_neighborhood_price()
```
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
```
Accumulation Pattern
* We're going to use accumulation pattern to accumulate the necessary data for
    our output.
* First, we need to define and initialize our accumulator called
    **average_price**. We also need to define and initialize a dictionary holder
    that will hold the neighborhood and a list of prices. Name this dictionary
    **neighborhood_prices**.
* Then we're going to open and read **filename** that was passed in the
    function.
    * Then we're going to iterate through each line of the data, starting from the
    second line, because the first line is the header.
        * While iterating, we're going to access the index that corresponds to
            neighborhood. We're store that data into a variable called
            **neighborhood**. This will be the key of the dict.
        * Also access the index that corresponds to price and store it in a
            variable called **price**. This will be the value of the dictionary
        * Construct the dictionary
            * Check to see if **neighborhood** is not in the
            **neighborhood_prices**
                * If it's not there, set it as a key and initialize its value
                    with an empty list.
            * Append the price to the empty list of the associated key.
        * After constructing **neighborhood_prices**, iterate through the keys
            and values of **neighborhood_prices** using items(). Using items()
            will let us access the keys and values of the dictionary.
            * construct the accumulator's keys and values by setting its key as
                the neighborhood and its value with the average of the list of
                prices. We're going to import mean from statistics to be able to
                use the mean() to get the average of the list.
* Return **average_price**

