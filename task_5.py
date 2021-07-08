"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("task_5.txt", 'w+') as file:
    file.write("1 2 3 4 5 6 7 8 9 10 11")

with open("task_5.txt") as file:
    content = file.read()
    content = map(int, content.split(' '))


print(sum(content))