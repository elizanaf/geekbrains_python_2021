"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

while True:
    n = int(input("Please, enter a number..."))
    if n > 0:
        break
    print("Try again...")


n = str(n)
n_2 = n + n
n_3 = n_2 + n

n = int(n)
n_2 = int(n_2)
n_3 = int(n_3)

print("Answer: ", n + n_2 + n_3)