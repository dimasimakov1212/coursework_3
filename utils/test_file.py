from function import import_data, data_for_work, sorted_data, print_date
from main import file_input

# проверяем загрузку данных и вид данных
# a = (import_data(file_input))
# b = a[0]
# print(b)
# for key, item in b.items():
#     print(key, item)

# проверка формирования нового списка данных
# a = (import_data(file_input))
# print(data_for_work(a))
# for item in data_for_work(a):
#     print(item)

# проверка сортировки списка словарей по дате
a = import_data(file_input)
b = data_for_work(a)
c = sorted_data(b)
for item in c:
    print(item)

# проверка вывода информации из словаря
date = print_date(c[0])

