"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

program_running = True

while program_running:
    sales_taken = int(input("Enter sales: $"))
    SALES_TARGET = 1000

    if sales_taken < 0:

        program_running = False

    else:
        if sales_taken < SALES_TARGET:

            bonus_rate = 0.1

        else:

            bonus_rate = 0.15

        bonus_amount = float(sales_taken) * bonus_rate
        bonus_amount = int(bonus_amount)

        print(bonus_amount)

