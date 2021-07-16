"""1. Создать класс TrafficLight (светофор)
и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать
как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
описанный метод.Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import itertools
import time
from PIL import Image

class TrafficLight:
        def __init__(self):
            self._color = 'RED'


        def running(self):
            for el in itertools.cycle((0, 1, 2)):
                image = Image.open("red.png")
                image.show()
                print("Waiting for 7 seconds before YELLOW color")
                time.sleep(7)
                self._color = 'YELLOW'
                image.close()
                image = Image.open("yellow.png")
                image.show()
                print("Waiting for 2 seconds before GREEN color")
                time.sleep(2)
                self._color = 'GREEN'
                image.close()
                image = Image.open("green.png")
                image.show()
                print("Waiting for 5 seconds before RED color")
                time.sleep(5)
                self._color = 'RED'


a = TrafficLight()
a.running()