import threading
from time import sleep


class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        if isinstance(name, str):
            self.name = name
        if isinstance(power, int):
            self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        enemies = 100
        days = 0
        while enemies != 0:
            enemies -= self.power
            days += 1
            print(f'{self.name}, сражается {days} день(дня)..., осталось {enemies} воинов')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")