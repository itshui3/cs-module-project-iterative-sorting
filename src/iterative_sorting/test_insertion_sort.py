import unittest
# test functionality
import random
# to generate random nums
from insertion_sort import *

class InsertionSortTest(unittest.TestCase):

    def test_insert_sort(self):
        unsorted1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        unsorted2 = []
        unsorted3 = [1, 5, -2, 4, 3]
        unsorted4 = random.sample(range(200), 50)

        self.assertEqual(insertion_sort(unsorted1), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(insertion_sort(unsorted2), [])
        self.assertEqual(insertion_sort(unsorted3), [-2, 1, 3, 4, 5])
        self.assertEqual(insertion_sort(unsorted4), sorted(unsorted4))


if __name__ == '__main__':
    unittest.main()
