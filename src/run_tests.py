# build a cli script to run all tests

from sys import argv, path
import os

root = '/'.join([i for i in __file__.split('/') if i != 'src' and i != 'run_tests.py'])

test_dirs = [root + '/src/iterative_sorting', root + '/src/searching', root + '/src/testing_stuff']
# if cli arguments specified, use to determine which tests to run

for i in test_dirs:
    path.append(i)

import test_insertion_sort, test_iterative, test_searching, test_quikmaths
print(test_insertion_sort)
# import unittest

# test_suites = []

# if 'insertion_sort' in argv:
#     test_suites.append(unittest.TestLoader().loadTestsFromTestCase(test_insertion_sort))

# for i in test_suites:
#     unittest.TextTestRunner(verbosity=2).run(i)

# unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(test_insertion_sort))
    