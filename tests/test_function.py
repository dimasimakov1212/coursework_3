import unittest
from utils import function

# if __name__ == '__main__':
#     unittest.main()


class TestFunction(unittest.TestCase):

    def test_print_date(self):
        self.assertEqual(function.print_date({'date': '2019-08-26T10:50:58.294041'}), '26.08.2019')

    def test_data_for_work(self):
        list_in = [{'id': 441945886, 'state': 'EXECUTED',
                    'date': '2019-08-26T10:50:58.294041',
                    'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                    'description': 'Перевод организации',
                    'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
                   {'id': 615064591, 'state': 'CANCELED',
                    'date': '2018-10-14T08:21:33.419441',
                    'operationAmount': {'amount': '77751.04', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                    'description': 'Перевод с карты на счет',
                    'from': 'Maestro 3928549031574026', 'to': 'Счет 84163357546688983493'}]

        list_out = [{'id': 441945886, 'state': 'EXECUTED',
                     'date': '2019-08-26T10:50:58.294041',
                     'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                     'description': 'Перевод организации',
                     'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}]
        self.assertEqual(function.data_for_work(list_in), list_out)

