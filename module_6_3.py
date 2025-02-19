import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self.speed <= 0 or dz < 0:
            print("It's too deep, i can't dive :(")
            self._cords = [0, 0, 0]
        else:
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed
            self._cords[0] = dx * self.speed

    def get_cords(self):
        print(f"X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        number_eggs = random.randint(1, 4)
        print(f"Here are(is) {number_eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        if self.speed <= 0:
            return
        self._cords[0] = int(self._cords[0] / self.speed)
        self._cords[1] = int(self._cords[1] / self.speed)
        self._cords[2] -= int(abs(dz) * self.speed / 2)
        if self.speed > 0:
            super().move(self._cords[0], self._cords[1], self._cords[2])


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

