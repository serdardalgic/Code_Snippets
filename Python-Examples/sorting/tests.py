import unittest
from merge_sort import merge_sort


class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.unsorted_list = [
            9, 1, 8, 2, 44, 3, 4, 7, 5, 6, 32, 21]

    def test_mergesort(self):
        result = merge_sort(self.unsorted_list)
        for i in range(1, len(result)):
            if result[i - 1] > result[i]:
                self.fail("mergesort has failed.")

if __name__ == '__main__':
    unittest.main()
