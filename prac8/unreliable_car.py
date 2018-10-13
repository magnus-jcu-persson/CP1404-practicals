from practicals.prac6.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):

        chance_to_drive = randint(0, 100)

        if chance_to_drive < self.reliability:
            return super().drive(distance)
        else:
            return 0
