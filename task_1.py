"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

def countSalary(hours, payment_per_hour, prize):
    try:
        hours = float(hours)
        payment_per_hour = float(payment_per_hour)
        prize = float(prize)
    except ValueError:
        return False

    return(float(hours) * float(payment_per_hour)) + float(prize)

filename, hours, payment_per_hour, prize = argv

if not countSalary(hours, payment_per_hour, prize):
    print("Value Error.")
    exit(1)

print(countSalary(hours, payment_per_hour, prize))