import unittest
import sys
import os
from unittest.mock import MagicMock,patch
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.main.model.JsonRequests import GetRank

class ModelTests(unittest.TestCase):

    def setUp(self):
        self.rank = GetRank()

    def test_get_init_rank_success(self):
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_get.return_value = mock_response
            response = self.rank.get_init_rank()
            self.assertEqual(response.status_code, 200)

    def test_get_init_rank_failure(self):
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response
            with self.assertRaisesRegex(requests.exceptions.HTTPError, "Request failed with status code: 404"):
                self.rank.get_init_rank()

    def test_get_people_from_rank(self):
        with patch.object(self.rank, 'get_init_rank', return_value=MagicMock
                          (json=lambda: {'items': [{'personId': '2005AUST01'}]})):
            people = self.rank.get_people_from_rank()
            self.assertEqual(people, ['2005AUST01'])

    def test_get_competition_for_everyone(self):
        with patch.object(self.rank, 'get_people_from_rank', return_value=['2005AUST01']):
            with patch('requests.get') as mock_get:
                mock_response = MagicMock()
                mock_response.json.return_value = {'name': 'Anthony Austin', 'results': 
                                                   {'CaltechDallas2005': {'333': [{'average': 8078}]}}}
                mock_get.return_value = mock_response
                competitions = self.rank.get_competition_for_everyone()
                self.assertEqual(competitions, {'Anthony Austin': {'CaltechDallas2005':
                                                                    {'333': [{'average': 8078}]}}})        





if __name__ == '__main__':
    unittest.main()