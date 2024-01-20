import unittest
from src.main.model.JsonRequests import GetRank

class ModelTests(unittest.TestCase):
    
    def __init__(self):
        self.response = GetRank.print_result()

    def test_average_of_zero(self):
        print()



if __name__ == '__main__':
    unittest.main()