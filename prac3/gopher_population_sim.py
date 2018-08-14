"""
GPS - Gopher Population Simulator
Calculates and displays the population of gophers over a yearly period.
"""
import random
def main():

    population = 1000
    MIN_YEARLY_BORN = 0.10
    MAX_YEARLY_BORN = 0.20
    MIN_YEARLY_DEATH = 0.05
    MAX_YEARLY_DEATH = 0.25

    REPORTING_YEARS = 10

    print('Starting Population:', population)
    for year in range(REPORTING_YEARS):

        gophers_born = calculate_population_change(population, MIN_YEARLY_BORN, MAX_YEARLY_BORN)
        gophers_died = calculate_population_change(population, MIN_YEARLY_DEATH, MAX_YEARLY_DEATH)

        population -= gophers_died
        population += gophers_born

        print('YEAR', year + 1)
        print("{0} gophers were born. {1} died.".format(gophers_born, gophers_died))
        print("Population:", population)

def calculate_population_change(population, min, max):

    percentage = random.randint(min*100, max*100) / 100
    return int(population * percentage)


main()