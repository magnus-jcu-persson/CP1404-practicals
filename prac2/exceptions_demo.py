"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

Value error will occur when input is not a numeric character

2. When will a ZeroDivisionError occur?

When the denominator is a 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

I could. and have below.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print('Invalid, denominator cannot be a zero.')
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")