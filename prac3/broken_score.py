"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():

    score = int(input("Enter score: "))

    print(get_score_results(score))


def get_score_results(score):
    if score > 100 or score < 0:
        result = "Invalid Score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
