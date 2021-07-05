 
"""5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

proceeds = input("Enter proceeds: ")
costs = input("Enter costs: ")

proceeds = float(proceeds)
costs = float(costs)

if proceeds < 0 or costs < 0:
    print("ERROR.")

if proceeds == 0 and costs == 0:
    print("No proceeds, no costs...")
    exit(1)

if proceeds > costs:
    print("The proceeds of the firm exceed costs.")
    profit = proceeds - costs
    profitability = profit / proceeds
    print("Profitability is", profitability)

    count_of_employees= input("Enter the count of employees... ")
    count_of_employees = int(count_of_employees)
    profit_of_employee = profit / count_of_employees
    print("Profit of each employee is", profit_of_employee)
else:
    print("The costs of the firm exceed proceeds.")