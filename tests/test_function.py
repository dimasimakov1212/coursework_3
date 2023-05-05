import unittest
from utils import function

if __name__ == '__main__':
    unittest.main()


class TestFunction(unittest.TestCase):

    def test_print_date(self):
        self.assertEqual(function.print_date({'date': '2019-08-26T10:50:58.294041'}), '26.08.2019')
        self.assertEqual(function.print_date({'date': '2019-07-16T10:50:58.294041'}), '16.07.2019')
        self.assertEqual(function.print_date({'date': '2018-01-05T10:50:58.294041'}), '05.01.2018')
        self.assertEqual(function.print_date({'date': '2017-01-05T10:50:58.294041'}), '05.01.2017')
