"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def isFloat(number):
    try:
        float(number)
        return True
    except ValueError:
        print("Not a number...")
        exit(0)


def division(dividend, divider):
    """
    Division of the number.

    :param dividend: float
    :param divider: float
    :return: float
    """

    return dividend/divider


divident = input("Please, enter a divident...")

if isFloat(divident):
    divident = float(divident)

divider = input("Please, enter a divider...")

if isFloat(divider):
    divider = float(divider)

if divider == 0:
    print("The divider cannot be 0.")
    exit(1)

print("Answer: ", division(divident, divider))
