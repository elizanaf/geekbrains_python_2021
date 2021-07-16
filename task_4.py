"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car goes!")

    def stop(self):
        print("Car stops!")

    def turn(self, direction):
        if direction == "right":
            print("Car turns to the right!")
        elif direction == "left":
            print("Car turns to the left!")
        else:
            print("Not possible direction!")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Speed is too high!")
        else:
            print(self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speed is too high!")
        else:
            print(self.speed)

class PoliceCar(Car):
    pass


car_1 = TownCar(70, "black", "Mersedes Benz", False)
car_2 = SportCar(120, "red", "Lamborgini", False)
car_3 = PoliceCar(90, "white", "Toyota", True)
car_4 = WorkCar(30, "blue", "Honda", False)

print("Town Car:\n" + car_1.name + '\n' + str(car_1.speed) + '\n' + car_1.color + '\n' + "Is police: " + str(car_1.is_police))

car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_4.show_speed()

car_3.go()
car_4.stop()
car_1.turn("right")
car_2.turn("left")
car_4.turn("up")
