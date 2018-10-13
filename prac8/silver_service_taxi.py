from practicals.prac8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50

    def __init__(self, name, fuel):
        super().__init__(name, fuel)

    def __str__(self):
        taxi_string = super().__str__()

        return "{} plus a flagfall of ${:.2f}".format(super().__str__(), self.flag_fall)

    def get_fare(self):

        return super().get_fare() + self.flag_fall