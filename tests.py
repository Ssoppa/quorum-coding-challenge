import unittest

class TestBillVisualizatorMethods(unittest.TestCase):
    def setUp(self):
        # Create a BillVisualizator object, with default paths
        pass

    def test_prepare_data(self):
        # call method
        # for each dataframe, check the values
        pass
        
    def test_get_first_deliverable(self):
        # call method
        # check if the returned list is correct
        pass

    def test_get_second_deliverable(self):
        # call method
        # check if the returned list is correct
        pass

if __name__ == '__main__':
    unittest.main()

# TODO's:
# - Change methods to also return a list with the values in the csv
# - Check correct values in the provided files
# - Update tests based on these values
# - Create a class to test the initialization with incorrect values (e.g. wrong filepath)
