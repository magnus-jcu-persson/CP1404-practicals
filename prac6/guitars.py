from guitar_test import Guitar


def main():
    print('Guitars!')
    guitars = []
    user_choice = ""
    while user_choice != "Q":

        print("A - Add Guitar",
              "L - List Guitars",
              "Q - Quit",
              sep="\n")
        user_choice = input(">>> ").upper()
        if user_choice == "A":
            add_guitar(guitars)

        elif user_choice == "L":
            display_guitars(guitars)

        elif user_choice == "Q":
            print("BYE")

        else:
            print("Invalid Choice")


def add_guitar(guitars):
    guitar = Guitar(input('Name: '),
                     input('Year: '),
                     float(input('Cost: ')))

    guitars.append(guitar)
    print("{} added".format(guitar))


def display_guitars(guitars):
    print(guitars)
    print("My Guitars:")
    for i, guitar in enumerate(guitars):
        print("Guitar {}: {}".format(i + 1, guitar))



main()
