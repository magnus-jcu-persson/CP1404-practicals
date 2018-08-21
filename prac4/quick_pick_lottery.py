import random
def main():

    MIN_RANGE = 1
    MAX_RANGE = 45
    DRAWS_PER_RANGE = 6

    drawn_numbers = []

    rounds = int(input("How many quick picks? "))

    for i in range(rounds):
        round_numbers = []
        while len(round_numbers) < DRAWS_PER_RANGE:
            number = random.randint(MIN_RANGE, MAX_RANGE)
            if number not in drawn_numbers:
                round_numbers.append(str(number))
                drawn_numbers.append(number)

        round_numbers.sort()
        print(' '.join(round_numbers))

main()