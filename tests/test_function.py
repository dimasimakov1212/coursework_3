import unittest
from utils import function

# if __name__ == '__main__':
#     unittest.main()


class TestFunction(unittest.TestCase):

    def test_print_date(self):
        self.assertEqual(function.print_date({'date': '2019-08-26T10:50:58.294041'}), '26.08.2019')

    def test_data_for_work(self):
        list_in = [{'id': 441945886, 'state': 'EXECUTED'},
                   {'id': 615064591, 'state': 'CANCELED'},
                   {}]

        list_out = [{'id': 441945886, 'state': 'EXECUTED'}]

        self.assertEqual(function.data_for_work(list_in), list_out)

    def test_sorted_data(self):
        list_in = [{'date': '2019-08-26T10:50:58.294041'},
                   {'date': '2019-07-03T18:35:29.512364'},
                   {'date': '2018-06-30T02:08:58.425572'},
                   {'date': '2018-03-23T10:45:06.972075'},
                   {'date': '2019-04-04T23:20:05.206878'},
                   {'date': '2019-03-23T01:09:46.296404'}]

        list_out = [{'date': '2018-06-30T02:08:58.425572'},
                    {'date': '2019-03-23T01:09:46.296404'},
                    {'date': '2019-04-04T23:20:05.206878'},
                    {'date': '2019-07-03T18:35:29.512364'},
                    {'date': '2019-08-26T10:50:58.294041'}]

        self.assertEqual(function.sorted_data(list_in), list_out)

    def test_print_description(self):
        dict_in = {'description': 'Перевод организации'}

        str_out = 'Перевод организации'

        self.assertEqual(function.print_description(dict_in), str_out)

