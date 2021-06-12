import unittest


from functions import dict_to_str, sort_by_freq


class TestFunctions(unittest.TestCase):

    def test_dict_to_word(self):
        dict1 = {'H': [1], 'l': [3,4], 'e': [2], 'o': [5]}
        dict2 = {'A': [1], 'r': [7], 't': [4], 'n': [2], 'e': [6], 'o': [3], 'h': [5]}
        dict3 = {'e': [4], 's': [5,3,2,6], 'A': [1]}
        self.assertEqual(dict_to_str(dict1), 'Hello')
        self.assertEqual(dict_to_str(dict2), 'Another')
        self.assertEqual(dict_to_str(dict3), 'Assess')


    def test_sort_by_freq(self):
        lst1 = [4,4,6,4,2,2,4,6]
        lst2 = [1,1,5,6,8,1,1,3,3,3,3]
        lst3 = [1,2,3,4,5]
        self.assertEqual(sort_by_freq(lst1), [4,4,4,4,6,6,2,2])
        self.assertEqual(sort_by_freq(lst2), [1,1,1,1,3,3,3,3,5,6,8])
        self.assertEqual(sort_by_freq(lst3), [1,2,3,4,5])

