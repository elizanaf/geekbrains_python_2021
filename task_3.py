"""Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:

    income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return str(self.name) + " " + str(self.surname)

    def get_total_income(self):
        return str(self._income["wage"] + self._income["bonus"])


position = Position("Olga", "Ivanova", "programmer", {"wage": 20000, "bonus": 10000})
print("Name: ", position.name)
print("Surname: ", position.surname)
print("Position: ", position.position)
print("Wage: ", position._income["wage"])
print("Bonus: ", position._income["bonus"])
print("Full name: ", position.get_full_name())
print("Total income: ", position.get_total_income())