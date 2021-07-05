"""2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

seconds = int(input("Please, enter time in seconds..."))

if seconds < 0:
    print("Invalid time")
    exit(0)

hours = seconds // 3600
minutes = seconds % 3600 // 60
tmp = seconds % 3600 % 60
seconds = tmp

print('Time in format hh:mm:ss: {0:02}:{1:02}:{2:02}' .format(hours, minutes, seconds))
