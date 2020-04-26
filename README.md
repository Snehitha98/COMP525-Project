### Method: highest_reviewed_listing()
```
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
```
#### Setting up first accumulator
* Initialize local variable `list_of_reviews_d` to empty dictionary
   * keys are unique neighborhood group
   * values are list of reviews corresponding to each neighborhood group
* We use it to :
   * Get all the reviews for each neighborhood group
   * Further process it to compute and return the dictionary that has details
     of name,price,neighborhood for maximum reviewed neighborhood group.

#### Get the data from the file
* `file_ref` holds a reference to the file object returned by open
* `file_ref` is used to open and read from the CSV file named `filename`

#### Understanding the text file structure
The text file is organized in lines
* First line has the column headings
* Remaining lines have the Airbnb data
* A line corresponds to a spreadsheet row and has `,` as delimiter between
  the row cells

#### Solution logic idea
Three accumulation patterns:
1. First, we compute the dictionary `list_of_reviews_d`
2. Second, we find the maximum review of each neighborhood group and assign the
   value of `highest_review_d` to maximum review with key `neighborhood_grp`.
3. Third, we compute `result_d` by iterating through `highest_review_d` to
   produce the listing details for each neighborhood_grp
4. Return `result_d`


#### More detailed logic steps to compute `list_of_reviews_d`
* Iterate through `file_ref` to get hold of each line except the heading line
  with loop variable `line`
    * At each iteration
        * Split `line` at `,` to get all the row cells in another list, named `line_row`
        * Extract from the 5th element of `line_row` (at index 4) the country
            name and store it in variable `neighborhood_grp`
        * Extract from the 12th element of `line_row` (at index 11) the country
            name and store it in variable `reviews`
        * Use the histogram pattern to update `list_of_reviews_d` such that:
            * if `neighborhood_grp` is in `list_of_reviews_d` append `reviews` to
              the value associated with existing key `neighborhood_grp`
            * else, add the key and set up its value to a list that has
              the `reviews`
* close the opened file `file_ref`

#### More detailed logic steps to compute `highest_review_d`
* Use for loop to iterate over `list_of_reviews_d` with loop variable `neighborhood_grp`
     * At each iteration
         * convert list of reviews which are strings to list of integers
           and store it in variable named `str_to_int`
         * Now, use max function to find maximum review of `str_to_int` and
           store it in `highest_review_d` with the same key `neighborhood_grp`

#### More detailed logic steps to compute `result_d`
* Iterate through `file_ref` to get hold of each line except the heading line
  with loop variable `line`
    * At each iteration
        * Split `line` at `,` to get all the row cells in another list, named `line_row`
        * Extract from the 2nd element of `line_row` (at index 1) the country
          name and store it in variable `name`
        * Extract from the 5th element of `line_row` (at index 4) the country
          name and store it in variable `neighborhood_grp`
        * Extract from the 6th element of `line_row` (at index 5) the country
          name and store it in variable `neighborhood`
        * Extract from the 10th element of `line_row` (at index 9) the country
          name and store it in variable `price`
        * Extract from the 12th element of `line_row` (at index 11) the country
          name and store it in variable `reviews`
        * Use for loop to iterate over `highest_review_d` with loop variable `key`
             * use if condition to check whether `reviews` are equal to `str(highest_review_d[key])`
                 * use if condition to check whether `neighborhood_grp` are equal to `key`
                     * Concatenate name,price and neighborhood and set up value of `result_d`
                       to list with the same key.

### closing the file
  * close the openend file `file_ref`
  * Return `result_d`
