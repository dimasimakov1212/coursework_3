import json


def import_data(file_name):
    """
    Загружает данные из файла формата json
    :param file_name: имя файла с данными
    :return: список с данными
    """
    with open(file_name, "r", encoding="utf-8") as file:
        file_with_data = json.load(file)

        return file_with_data


def data_for_work(input_list):
    """
    Подготавливает начальные данные для дальнейшей обработки
    предварительный отбор по статусу перевода EXECUTED
    исключает пустые строки
    :param input_list: начальный список
    :return: список для обработки
    """

    new_list = []
    for item in input_list:
        if not item:
            continue
        elif item["state"] == "EXECUTED":
            new_list.append(item)

    return new_list


def sorted_data(list_1):
    """
    Сортирует список по дате операции
    :param list_1: отобранный список
    :return: 5 последних операций
    """
    # сортирует список по дате
    sorted_list = sorted(list_1, key=lambda a: a["date"])

    # возвращаем список из 5 последних операций
    return sorted_list[-5:]


def print_operation(dict_one):
    """
    Принимает на вход словарь с данными и выводит
    в соответствии с требованиями
    :param dict_one:
    :return:
    """
    # преобразуем дату
    date_in = dict_one['date'][:10]
    date_out = date_in[-2:] + '.' + date_in[5:7] + '.' + date_in[:4]

    # вывод 1 строки в формате "дата" "назначение операции"
    print(date_out, dict_one['description'])

    # преобразуем поле 'from'
    try:
        from_in = dict_one['from']
        from_num = [num for num in from_in if num.isdigit()]
        from_text = "".join([num for num in from_in if num.isalpha()])
        from_num_len = len(from_num)

        # заменяем звездочками непечатаемые данные номера
        for item in range(6, from_num_len - 4):
            from_num[item] = '*'

        # разделяем номер группами по 4 цифры
        num_1 = "".join(from_num)
        from_num_print = ''
        for i in range(0, from_num_len, 4):
            from_num_print += num_1[i:i+4]
            from_num_print += ' '

        # итоговый вывод для печати "откуда"
        from_print = from_text + ' ' + from_num_print

    except KeyError:
        from_print = 'Нет данных '

    # преобразуем поле 'to'
    to_in = dict_one['to']
    to_num = "".join([num for num in to_in if num.isdigit()])
    to_text = "".join([num for num in to_in if num.isalpha()])

    # заменяем звездочками непечатаемые данные номера
    to_num_print = '**' + to_num[-4:]

    # итоговый вывод для печати "куда"
    to_print = to_text + ' ' + to_num_print

    # вывод второй строки в формате "откуда" -> "куда"
    print(f"{from_print}-> {to_print}")

    # вывод третьей строки в формате "сумма" "валюта"
    print(dict_one['operationAmount']['amount'],
          dict_one['operationAmount']['currency']['name'], end="\n")

    return None

