import unittest
# 
import random
# to generate random nums
from insertion_sort import *

class InsertionSortTest(unittest.TestCase):

    def test_insert_sort(self):
        unsorted1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        unsorted2 = []
        unsorted3 = [0, 1, 2, 3, 4, 5]
        unsorted4 = random.sample(range(200), 50)

        self.assertEqual(insertion_sort(unsorted1), [0,1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main()
