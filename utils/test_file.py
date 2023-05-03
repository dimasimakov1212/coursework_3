from function import import_data, data_for_work
from main import file_input

# проверяем загрузку данных и вид данных
# a = (import_data(file_input))
# b = a[0]
# print(b)
# for key, item in b.items():
#     print(key, item)

# проверка формирования нового списка данных
a = (import_data(file_input))
print(data_for_work(a))
for item in data_for_work(a):
    print(item)
