import json

class ListClass:
    """Класс ListClass
    Содержит два метода:
    1. get_sorted_list - Получает список словарей для работы из
    json файла с данными (operation.json). Сортирует операции по статусу 'EXECUTED'

    2. get_slice_list - Делает срез из 5-ти последних операций пользователя, используя
    список, отсортированный предыдущим методом
    """

    def __init__(self):
        """
        Инициализация класса
        """
        self.sorted_list = []


    def get_sorted_list(self):
        """
        Функция получает данные из файла operation.json, преобразовывает их в список
        словарей, фильтрует операции по статусу и сортирует по дате

        Возвращает готовый отсортированный по дате список словарей.
        """
        with open('operation.json', 'r', encoding='utf-8') as file:
            file_content = file.read()
            content_list = json.loads(file_content)
            new_content_list = []
            for item in content_list:
                if item != {} and item["state"] == "EXECUTED":
                    new_content_list.append(item)
            self.sorted_list = sorted(new_content_list, key=lambda x: x["date"], reverse=True)
            return self.sorted_list


    def get_slice_list(self):
        """
        Функция принимает список из предыдущего метода

        Возвращает срез из 5-ти последних операций пользователя (список из 5ти словарей)

        """
        actual_list = self.get_sorted_list()[0:5]
        return actual_list