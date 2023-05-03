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
