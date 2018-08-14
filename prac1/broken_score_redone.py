"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def original_code():
    # TODO: Fix this!

    score = float(input("Enter score: "))
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        if score > 50:
            print("Passable")
        if score > 90:
            print("Excellent")
        if score < 50:
            print("Bad")

def fixed_code():

    score = int(input("Enter score: "))

    if score > 100 or score < 0:
        print("Invalid Score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")


fixed_code()
