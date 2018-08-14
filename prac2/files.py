"""
Write a program that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

Write a program that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""

user_name = input("Please enter your name:").lower()

user_filename = user_name + '.txt'

with open('./' + user_filename, 'w') as out_file:

    print('Your name is', user_name.capitalize(), file=out_file)


"""
Create a text file called "numbers.txt" (You can create a simple text file in PyCharm with Ctrl+N, choose "File" and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens "numbers.txt", reads the numbers and adds them together then prints the result, which should be... 59.

Extended (perhaps only do this if you're cruising... if you are struggling, just read the solution) ...
Now extend your program so that it can print the total for a file containing any number of numbers.
"""

IN_FILE = 'numbers.txt'

total = 0
with open('./' + IN_FILE, 'r') as open_file:

    numbers = open_file.readlines()

    for number in numbers:
        total += int(number)

print(total)
