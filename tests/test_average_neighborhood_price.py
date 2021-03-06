"""
test_average_neighborhood_price.py
To test the average_neighborhood_price()
Carlo Capuz
Created 5/4/2020
"""

import unittest
from problems.carlo import NYCAirbnbListings

class TestTotalListingsInNeighborhoodGroup(unittest.TestCase):
    """
    Contains test functions for average_neighborhood_price()
    """

    def test_one_entry(self):
        """
        test 1 entry of data
        """

        nyc_airbnb_listing = NYCAirbnbListings()
        filename_1 = "data/air_bnb_1_data.csv"
        actual_result = nyc_airbnb_listing.average_neighborhood_price(filename_1)
        expected_result = {'Midtown': 225}
        self.assertDictEqual(actual_result, expected_result)

    def test_25_entry(self):
        """
        test 25 entries of data
        """

        nyc_airbnb_listing = NYCAirbnbListings()
        filename_25 = "data/air_bnb_25_data.csv"
        actual_result = nyc_airbnb_listing.average_neighborhood_price(filename_25)
        expected_result = {'Kensington': 149, 'Midtown': 225, 'Harlem': 150,
                           'Clinton Hill': 89, 'East Harlem': 135, 'Murray Hill': 200,
                           'Bedford-Stuyvesant': 90, "Hell's Kitchen": 82,
                           'Upper West Side': 99.67, 'Chinatown': 150, 'South Slope': 89,
                           'West Village': 120, 'Williamsburg': 219.5, 'Fort Greene': 215,
                           'Chelsea': 140, 'Crown Heights': 99, 'Park Slope': 106.67}
        self.assertDictEqual(actual_result, expected_result)

    def test_whole_data(self):
        """
        test whole data
        """

        nyc_airbnb_listing = NYCAirbnbListings()
        filename = "data/air_bnb.csv"
        actual_result = nyc_airbnb_listing.average_neighborhood_price(filename)
        expected_result = {'"Kensington"': 92.89, '"Midtown"': 282.72,
                           '"Harlem"': 118.97, '"Clinton Hill"': 181.89, '"East Harlem"': 133.2,
                           '"Murray Hill"': 220.96, '"Bedford-Stuyvesant"': 107.68,
                           '"Hell\'s Kitchen"': 204.79, '"Upper West Side"': 210.92,
                           '"Chinatown"': 161.5, '"South Slope"': 146.73, '"West Village"': 267.68,
                           '"Williamsburg"': 143.8, '"Fort Greene"': 151.37, '"Chelsea"': 249.74,
                           '"Crown Heights"': 112.48, '"Park Slope"': 176.31,
                           '"Windsor Terrace"': 138.99, '"Inwood"': 88.9, '"East Village"': 186.08,
                           '"Greenpoint"': 144.82, '"Bushwick"': 84.8, '"Flatbush"': 92.21,
                           '"Lower East Side"': 186.31, '"Prospect-Lefferts Gardens"': 110.4,
                           '"Long Island City"': 127.47, '"Kips Bay"': 202.41, '"SoHo"': 287.1,
                           '"Upper East Side"': 188.95, '"Prospect Heights"': 173.37,
                           '"Washington Heights"': 89.61, '"Woodside"': 85.1,
                           '"Brooklyn Heights"': 209.06, '"Carroll Gardens"': 175.91,
                           '"Gowanus"': 158.8, '"Flatlands"': 126.43, '"Cobble Hill"': 211.93,
                           '"Flushing"': 93.51, '"Boerum Hill"': 176.14, '"Sunnyside"': 84.87,
                           '"DUMBO"': 196.31, '"St. George"': 118.15, '"Highbridge"': 71.11,
                           '"Financial District"': 225.49, '"Ridgewood"': 77.18,
                           '"Morningside Heights"': 114.78, '"Jamaica"': 95.77,
                           '"Middle Village"': 109.58, '"NoHo"': 295.72,
                           '"Ditmars Steinway"': 95.03, '"Flatiron District"': 341.93,
                           '"Roosevelt Island"': 113.26, '"Greenwich Village"': 263.41,
                           '"Little Italy"': 222.07, '"East Flatbush"': 104.22,
                           '"Tompkinsville"': 76.19, '"Astoria"': 117.19,
                           '"Clason Point"': 112.76, '"Eastchester"': 141.69,
                           '"Kingsbridge"': 77.93, '"Two Bridges"': 127.07,
                           '"Queens Village"': 83.93, '"Rockaway Beach"': 132.18,
                           '"Forest Hills"': 121.62, '"Nolita"': 230.14,
                           '"Woodlawn"': 60.09, '"University Heights"': 69.57, '"Gravesend"': 79.01,
                           '"Gramercy"': 222.75, '"Allerton"': 87.6, '"East New York"': 85.43,
                           '"Theater District"': 248.01, '"Concourse Village"': 73.78,
                           '"Sheepshead Bay"': 105.77, '"Emerson Hill"': 68.2,
                           '"Fort Hamilton"': 93.82, '"Bensonhurst"': 75.79,
                           '"Tribeca"': 490.64, '"Shore Acres"': 152.71,
                           '"Sunset Park"': 113.04, '"Concourse"': 86.18, '"Elmhurst"': 80.46,
                           '"Brighton Beach"': 131.93, '"Jackson Heights"': 80.9,
                           '"Cypress Hills"': 128.9, '"St. Albans"': 100.83,
                           '"Arrochar"': 115, '"Rego Park"': 83.88,
                           '"Wakefield"': 85.58, '"Clifton"': 84.93, '"Bay Ridge"': 144.43,
                           '"Graniteville"': 68.67, '"Spuyten Duyvil"': 154.75,
                           '"Stapleton"': 98.96, '"Briarwood"': 105.88,
                           '"Ozone Park"': 85.27, '"Columbia St"': 162.95,
                           '"Vinegar Hill"': 187.18, '"Mott Haven"': 88.92, '"Longwood"': 91.92,
                           '"Canarsie"': 104.37, '"Battery Park City"': 367.56,
                           '"Civic Center"': 191.94, '"East Elmhurst"': 81.18,
                           '"New Springville"': 76, '"Morris Heights"': 76.94,
                           '"Arverne"': 171.78, '"Cambria Heights"': 81.73,
                           '"Tottenville"': 144.86, '"Mariners Harbor"': 94.62,
                           '"Concord"': 58.19, '"Borough Park"': 63.07,
                           '"Bayside"': 157.95, '"Downtown Brooklyn"': 150.35,
                           '"Port Morris"': 79.89, '"Fieldston"': 75.08,
                           '"Kew Gardens"': 88.38, '"Midwood"': 80.34,
                           '"College Point"': 88, '"Mount Eden"': 58.5, '"City Island"': 173,
                           '"Glendale"': 90.8, '"Port Richmond"': 90.11, '"Red Hook"': 143.46,
                           '"Richmond Hill"': 87.12, '"Bellerose"': 99.36, '"Maspeth"': 83.65,
                           '"Williamsbridge"': 96.75, '"Soundview"': 53.47, '"Woodhaven"': 67.17,
                           '"Woodrow"': 700, '"Co-op City"': 77.5, '"Stuyvesant Town"': 169.11,
                           '"Parkchester"': 69.08, '"North Riverdale"': 79.9,
                           '"Dyker Heights"': 93.42, '"Bronxdale"': 57.11,
                           '"Sea Gate"': 487.86, '"Riverdale"': 442.09,
                           '"Kew Gardens Hills"': 112.31, '"Bay Terrace"': 142, '"Norwood"': 75.55,
                           '"Claremont Village"': 87.46, '"Whitestone"': 107.55, '"Fordham"': 69.44,
                           '"Bayswater"': 87.47, '"Navy Yard"': 151.64, '"Brownsville"': 76.46,
                           '"Eltingville"': 141.67, '"Fresh Meadows"': 99.5, '"Mount Hope"': 77.5,
                           '"Lighthouse Hill"': 157.5, '"Springfield Gardens"': 94.24,
                           '"Howard Beach"': 115.4, '"Belle Harbor"': 171.5,
                           '"Jamaica Estates"': 182.95, '"Van Nest"': 113.82,
                           '"Morris Park"': 69.33, '"West Brighton"': 80.56,
                           '"Far Rockaway"': 165.86, '"South Ozone Park"': 82.4, '"Tremont"': 51.55,
                           '"Corona"': 59.17, '"Great Kills"': 100.6, '"Manhattan Beach"': 103.5,
                           '"Marble Hill"': 89.17, '"Dongan Hills"': 79.43,
                           '"Castleton Corners"': 139.75, '"East Morrisania"': 85,
                           '"Hunts Point"': 50.5, '"Neponsit"': 274.67,
                           '"Pelham Bay"': 105, '"Randall Manor"': 336, '"Throgs Neck"': 91.04,
                           '"Todt Hill"': 169, '"West Farms"': 122, '"Silver Lake"': 70,
                           '"Morrisania"': 83.44, '"Laurelton"': 95.33, '"Grymes Hill"': 159.14,
                           '"Holliswood"': 135.75, '"Pelham Gardens"': 93.61, '"Belmont"': 77.12,
                           '"Rosedale"': 76.69, '"Edgemere"': 94.73, '"New Brighton"': 101.8,
                           '"Midland Beach"': 91.83, '"Baychester"': 75.43, '"Melrose"': 83.3,
                           '"Bergen Beach"': 106.7, '"Richmondtown"': 78, '"Howland Hook"': 100,
                           '"Schuylerville"': 69.23, '"Coney Island"': 123.71,
                           '"New Dorp Beach"': 57.4, '"Prince\'s Bay"': 409.5,
                           '"South Beach"': 89.25, '"Bath Beach"': 81.76,
                           '"Jamaica Hills"': 132.12, '"Oakwood"': 81.2,
                           '"Castle Hill"': 63, '"Hollis"': 88.64, '"Douglaston"': 82.75,
                           '"Huguenot"': 118.33, '"Olinville"': 64, '"Edenwald"': 82,
                           '"Grant City"': 57.67, '"Westerleigh"': 71.5,
                           '"Bay Terrace  Staten Island"': 102.5, '"Westchester Square"': 122.2,
                           '"Little Neck"': 75.2, '"Fort Wadsworth"': 800, '"Rosebank"': 111.86,
                           '"Unionport"': 137.14, '"Mill Basin"': 179.75, '"Arden Heights"': 67.25,
                           '"Bull\'s Head"': 47.33, '"New Dorp"': 57, '"Rossville"': 75,
                           '"Breezy Point"': 213.33, '"Willowbrook"': 249}
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
