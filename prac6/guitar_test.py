class Guitar:
    def __init__(self, name='', year=1900, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2018 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

if __name__ == 'main':

    gibson = Guitar('Gibson L-5 CES', 1922, 16035.40)
    a_guitar = Guitar('Another Guitar', 2012, 2000.00)

    print(gibson.name,':', gibson.get_age())
    print(a_guitar.name,':', a_guitar.get_age())
    print(gibson.name,':', gibson.is_vintage())
    print(a_guitar.name,':', a_guitar.is_vintage())