import json


def import_data(file_name):
    """
    Загружает данные из файла формата json
    :param file_name:
    :return:
    """
    with open(file_name, "r", encoding="utf-8") as file:
        file_with_data = json.load(file)

        return file_with_data
