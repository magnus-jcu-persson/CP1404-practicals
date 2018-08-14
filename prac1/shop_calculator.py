"""
Simple calculator that asks the user how many shop items,
then runs through each items price and then returns the sum of those items.
"""
number_of_items = -1

while number_of_items < 0:
    number_of_items = int(input("Number of items: "))

    if number_of_items < 0:
        print("Invalid number of items!")

sum_of_items = 0.00
for i in range(0, number_of_items):
    sum_of_items += float(input("Price of item: "))

if sum_of_items > 100:
    discount_rate = 0.1
else:
    discount_rate = 0

sum_of_items -= (sum_of_items * discount_rate)

print("Total price for", number_of_items, "is", "$" + str(sum_of_items))



