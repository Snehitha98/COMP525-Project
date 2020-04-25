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
                * If it's not there, initialize its value by 1.
                * If it is there, increment its value by 1.
* Return **total_listings**