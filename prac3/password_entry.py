"""
Magnus Persson
"""
def main():

    valid = False
    MIN_LENGTH = 7
    while not valid:
        user_password = input('Password')

        if len(user_password) >= MIN_LENGTH:
            valid = True
            print("ALL GOOD")
        else:
            print("NOT ENOUGH LENGTH")

main()