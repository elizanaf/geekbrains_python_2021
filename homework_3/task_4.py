"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

n = input("Please, enter a number...")

max = 0
for idx, el in enumerate(n):
    if int(el) > int(max):
        max = el

print("Max is: ",max)