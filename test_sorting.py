import unittest
from insertion_sort import insertion_sort

class InsertionSortTestCase(unittest.TestCase):
    """ Insertion sort tests """

    def test_basic(self):
        unsorted = [7,6,2,3,4,1,5]
        self.assertEqual([1,2,3,4,5,6,7], insertion_sort(unsorted))

        u = [9,5,2341,1,4,31,8,9,4,4,4,4,8,39,1,2,3,4,36]
        self.assertEqual(sorted(u), insertion_sort(u))

if __name__ == '__main__':
    unittest.main()
