from function import import_data, data_for_work, sorted_data

# Имя файла с исходными данными
file_input = "operations.json"


# загружаем данные из файла
data_input = import_data(file_input)

# предварительная обработка данных
data_start = data_for_work(data_input)

# сортируем список операций по дате и берем 5 последних операций
data_out = sorted_data(data_start)

#
# вывод 1 строки в формате "дата" "назначение операции"
# вывод второй строки в формате "откуда" -> "куда"
# вывод третьей строки в формате "сумма" "валюта"