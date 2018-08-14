"""
Electricity Bill Estimator
Calculates bill amount based on several variables.
Two versions, first without tariff checks and second including.
FYI - kwh = Kilowatt Hours
"""

def bill_estimator_v1():

    print("Electricity Bill Estimator")

    cents_per_kwh = int(input("Enter cents per kWh: "))
    daily_kwh_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    daily_cents = (cents_per_kwh * daily_kwh_use)
    total_cents = (billing_days * daily_cents)



    total_dollars = total_cents / 100
    total_dollars = round(total_dollars, 2)

    print("Estimated bill:", "$" + "{0:.2f}".format(total_dollars))

def bill_estimator_v2():

    TARIFF_11 = 24.4618
    TARIFF_31 = 13.6928

    print("Electricity Bill Estimator 2.0")

    cents_per_kwh = -1
    while cents_per_kwh < 0:
        tariff = int(input("Which tariff? 11 or 31:"))

        if tariff == 11:
            cents_per_kwh = TARIFF_11
        elif tariff == 31:
            cents_per_kwh = TARIFF_31
        else:
            print("INVALID TARIFF")

    daily_kwh_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    daily_cents = (cents_per_kwh * daily_kwh_use)
    total_cents = (billing_days * daily_cents)



    total_dollars = total_cents / 100
    total_dollars = round(total_dollars, 2)
    print("Estimated bill: ${:.2f}".format(total_dollars))

bill_estimator_v1()
bill_estimator_v2()