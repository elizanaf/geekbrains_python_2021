"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

with open("task_7.txt") as file:
    average = 0
    count_of_firms = 0
    dict_profit = {}
    dict_average = {}
    for el in file:
        count_of_firms += 1
        name, code, income, costs = el.split()
        income, costs = int(income), int(costs)
        profit = income - costs
        if profit >= 0:
            average += profit
        dict_profit[name] = profit

    average /= count_of_firms
    dict_average["average_profit"] = average

my_list = [dict_profit, dict_average]

with open("task_7.json", 'w') as write_json:
    json.dump(my_list, write_json)