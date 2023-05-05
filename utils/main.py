from function import import_data, data_for_work, sorted_data, print_date
from function import print_description, print_from, print_to, print_amount, print_currency

# Имя файла с исходными данными
file_input = "operations.json"


# загружаем данные из файла
data_input = import_data(file_input)

# предварительная обработка данных
data_start = data_for_work(data_input)

# сортируем список операций по дате и берем 5 последних операций
data_out = sorted_data(data_start)

# вывод информации по операциям
for item in range(4, 0, -1):

    # вывод 1 строки в формате "дата" "назначение операции"
    print(f"{print_date(item)} {print_description(item)}")

    # вывод второй строки в формате "откуда" -> "куда"
    print(f"{print_from(item)}-> {print_to(item)}")

    # вывод третьей строки в формате "сумма" "валюта"
    print(f"{print_amount(item)} {print_currency(item)}")
