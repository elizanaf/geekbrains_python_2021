"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def generator(number):
    """Generator.
    :param number: int
    :return:
    """
    tmp = number
    while tmp != 0:
        yield tmp
        tmp -= 1


def factorial(list):
    """Counts the factorial of the number.
    :param list:
    :return:
    """
    tmp = 1
    for el in list:
        tmp *= el

    print("Factorial of the number is",tmp, '.')


number = input("Please, enter a numer...")

try:
    number = int(number)
except ValueError as e:
    print(e)
    exit(1)

g = generator(number)

factorial(g)