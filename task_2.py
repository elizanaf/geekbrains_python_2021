"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

file = open("task_2.txt", 'r')

count_of_lines = 0

for el in file:
    count_of_lines += 1
    print(str(count_of_lines) + " line contains " + str(len(el.split(' '))) + " words: " + el)

print("Count of lines: ", count_of_lines)