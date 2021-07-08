"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import cycle

def read_list():
    """Reads the list.
    :return:
    """

    list = []
    while True:
        tmp = input("Please, enter the element of the list...")
        if tmp == '':
            return list
        list.append(tmp)



my_list = read_list()

end_count = input("Please, enter the end count...")

try:
    end_count = int(end_count)
except ValueError as e:
    print(e)
    exit(1)

count = 0

for el in cycle(my_list):
    if count > end_count:
        break
    print(el)