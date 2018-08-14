def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    print()

def main():
    user_name = input("Enter name: ")

    user_choice = "A"
    while user_choice != "Q":

        display_menu()
        user_choice = input(">>> ").upper()

        if user_choice == "H":
            print("Hello", user_name)

        elif user_choice == "G":
            print("Goodbye", user_name)

        elif user_choice == "Q":
            print("FINISHED")

        else:
            print("Invalid Choice")

main()

