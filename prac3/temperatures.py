"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = "C - Convert Celsius to Fahrenheit\n" \
           "F - Convert Fahrenheit to Celsius\n" \
           "Q - Quit\n"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))

            display_fahrenheit(celsius)
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.

            fahrenheit = float(input("Fahrenheit: "))
            display_celsius(fahrenheit)


        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def display_fahrenheit(celsius):
    value = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(value))


def display_celsius(fahrenheit):
    value = 5 / 9.0 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(value))


main()