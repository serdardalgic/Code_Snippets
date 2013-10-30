import unittest
import filesearch


class BigFileSearchTest(unittest.TestCase):
    def test_calculate_len_of_strs(self):
        string = "Red$Beacon$Rocks"
        exp_rv = "3 6 5"
        rv = filesearch.calculate_len_of_strs(
            string.strip().split('$'))
        self.assertEqual(exp_rv, rv)


if __name__ == '__main__':
    unittest.main()
