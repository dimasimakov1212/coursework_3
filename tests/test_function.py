import unittest
from utils import function

# if __name__ == '__main__':
#     unittest.main()


class TestFunction(unittest.TestCase):

    def test_print_date(self):
        self.assertEqual(function.print_date({'date': '2019-08-26T10:50:58.294041'}), '26.08.2019')

