# Тема проекта: приложение «Касса кинотеатра».
# Спроектировать ПО, предназначенное для автоматизации деятельности кассы
# кинотеатра. Функции, которые должны быть реализованы в приложении:
# добавление, удаление, редактирование и просмотр информации о сеансах,
# наличии билетов и свободных мест

class Cinema:
    def __init__(self, name, location):
        self.name: str = name
        self.location: str = location


class Sessions(Cinema):
    def __init__(self, name_of_session, places, ticket, hall_number, time):
        super().__init__('PLAZZA', 'MINSK')
        self.name_of_session = name_of_session
        self.places = places
        self.ticket = ticket
        self.hall_number = hall_number
        self.time: float = time

    def info(self):
        print(f'Название кинотеатра - {self.name}\n'
              f'Название сеанса - {self.name_of_session}\n'
              f'Месторасположение кинотеатра - {self.location}\n'
              f'Зал - {self.hall_number}\n'
              f'Время сеанса - {self.time}')

    def replace_session(self, new_session_name):
        old_session_name = self.name_of_session
        self.name_of_session = new_session_name
        print(f'Сеанс {old_session_name} заменен на сеанс {new_session_name}')

    def replace_time(self, new_time):
        old_time = self.time
        self.time = new_time
        print(f'Время сеанса {old_time} заменено {new_time}')

    def delete_session(self):
        del self.name_of_session
        self.places = 0
        self.ticket = 0
        self.time = 0.0
        self.hall_number = 0
        print('Сеанс удален')

    def add_session(self, new_session_name, hall_number, time, places):
        self.name_of_session = new_session_name
        self.hall_number = hall_number
        self.time = time
        self.places = places
        print(f'Сеанс - {new_session_name}\n'
              f'добавлен в зал - {hall_number}\n'
              f'количество мест - {places}\n'
              f'время - {time}')

    def buy_ticket(self, amount):
        self.ticket -= amount
        self.places -= amount
        print(f'Купленно билетов - {amount}\n'
              f'Осталось билетов - {self.ticket}\n'
              f'Осталось свободных мест - {self.places}')


kino = Sessions('БЭТМЕН 2', 100, 100, 2, 14.22)
kino.info()
kino.replace_session('Cупермен')
kino.info()
kino.buy_ticket(55)
kino.delete_session()
kino.add_session('Ирония судьбы', 3, 22.59, 60)
kino.info()
kino.replace_time(22.45)
kino.delete_session()
