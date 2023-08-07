
class Data:
    """
    Класс Data (Данные)

    Работает с данными из операции пользователя
    Имеет 3 метода:

    1. get_date - возвращает дату совершения операции

    2. get_hide_account - зашифровывает номер счета, куда был совершен
    перевод денежных средств

    3. get_hide_card_number - зашифровывает номер карты или счета, откуда
    был совершен перевод денежных средств
    """

    def __init__(self, date, account, description, amount, name, card_number=None):
        """
        Инициализация класса
        :param date: Дата совершения операции
        :param account: Номер счета на который поступают ДС
        :param description: Описание операции
        :param amount: Сумма
        :param name: Денежная единица
        :param card_number: Номер карты или счета откуда совершен перевод ДС
        """
        self.date = date
        self.card_number = card_number
        self.account = account
        self.description = description
        self.amount = amount
        self.name = name


    def __repr__(self):
        return f'''{self.get_date()} {self.description}, 
{self.get_hide_card_number()} -> {self.get_hide_account()}
{self.amount} {self.name}'''


    def get_date(self):
        """
        Функция обрабатывает список операций

        :return: Возвращает дату совершения операции
        """
        string = self.date[:10]
        string = string.split('-')
        year = int(string[0])
        month = int(string[1])
        day = int(string[2])
        return f'{day}.{month}.{year}'


    def get_hide_account(self):
        """
        Функция обрабатывает список операций, получает
        и зашифровывает номер счета, на который поступают ДС

        :return: Возвращает зашифрованный номер счета.
        """
        new_list = self.account.split()
        actual_string = new_list[-1]
        return f'{new_list[0]} **{actual_string[-5:-1]}'


    def get_hide_card_number(self):
        """
        Функция обрабатывает список данных, получает и
        зашифровывает номер карты или счета, с которого
        совершен перевод ДС

        :return: Возвращает зашифрованный номер карты или счета.
        """
        if self.card_number:
            new_list = self.card_number.split()
            if len(new_list) > 2:
                actual_string = new_list[-1]
                return f'{new_list[0]} {new_list[1]} {actual_string[:5]} {actual_string[5:7]}** **** {actual_string[-5:-1]}'
            else:
                actual_string = new_list[-1]
                return f'{new_list[0]} {actual_string[:5]} {actual_string[5:7]}** **** {actual_string[-5:-1]}'
