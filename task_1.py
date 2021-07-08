"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

def readData():
    my_list = []
    while True:
        read = input("Please, enter some data to write to the file...")
        if read == '':
            break
        my_list.append(read + '\n')
    return my_list

file = open("task_1.txt", 'w')

file.writelines(readData())