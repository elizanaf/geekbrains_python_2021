"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

file = open("task_3.txt", 'r')

average = 0
count_of_lines = 0

for el in file:
    count_of_lines += 1
    salary = int(el.split(':')[1])
    average += salary
    if salary < 20000:
        print(el.split(':')[0])

average /= count_of_lines

print("Average: ", average)