def original():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print("END")

def looper(start, end, bounce):

    for i in range(start, end, bounce):

        print(i, end=' ')

    print('END')

def stars(amount):

    line_index = 1

    for n in range(amount):
        output_msg = ''
        for i in range(line_index):
            output_msg += '*'

        print(output_msg)
        line_index += 1

def stars_modified(amount):

    star_str = '*'
    for n in range(amount):

        print('*' * (n+1))



original()

print("FIRST LOOP")
looper(0, 110, 10)

print("SECOND LOOP")
looper(20, 0, -1)

print("STARS")
stars_amount = int(input("How many stars? #"))
stars(stars_amount)

stars_modified(4)