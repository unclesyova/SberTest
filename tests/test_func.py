import unittest


from functions import dict_to_str


class TestFunctions(unittest.TestCase):

    def test_dict_to_word(self):
        dict1 = {'H': [1], 'l': [3,4], 'e': [2], 'o': [5]}
        dict2 = {'A': [1], 'r': [7], 't': [4], 'n': [2], 'e': [6], 'o': [3], 'h': [5]}
        dict3 = {'e': [4], 's': [5,3,2,6], 'A': [1]}
        self.assertEqual(dict_to_str(dict1), 'Hello')
        self.assertEqual(dict_to_str(dict2), 'Another')
        self.assertEqual(dict_to_str(dict3), 'Assess')

