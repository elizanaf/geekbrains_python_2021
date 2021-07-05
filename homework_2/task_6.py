"""6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

result_a = input("Enter the first result: ")
result_b = input("Enter the second result: ")

result_a = float(result_a)
result_b = float(result_b)

if result_a <= 0:
    print("ERROR.")
    exit(1)

day = 1

while result_a < result_b:
    result_a += result_a * 0.1
    day = day + 1
    print(day, result_a)


print("DAY:", day)