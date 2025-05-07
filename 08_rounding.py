import math


# functions
def round_up(amount, round_val):
    """Rounds amount to desired whole number"""
    return int(math.ceil(amount / round_val)) * round_val


# main routine

# loop testing
while True:
    quantity_made = int(input("# of items"))
    total_expenses = float(input("Total expenses: "))
    target = float(input("Profit goal: "))
    round_to = int(input("Round to: "))

    selling_price = (total_expenses + target) / quantity_made
    suggested_price = round_up(selling_price, round_to)

    print(f"Minimum price: ${selling_price:.2f}")
    print(f"Suggested price: ${suggested_price:.2f}")
    print()
