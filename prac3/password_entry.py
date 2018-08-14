"""
Magnus Persson
"""
def main():

    valid = False

    while not valid:
        password = get_password()
        valid = check_password(password)



def get_password():
    user_password = input('Password')
    return user_password

def check_password(password):
    MIN_LENGTH = 7

    if len(password) >= MIN_LENGTH:
        print("ALL GOOD")
        return True
    else:
        print("NOT ENOUGH LENGTH")
        return False


main()