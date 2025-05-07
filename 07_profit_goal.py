# functions
def yes_no_check(question):
    """Checks that user inputs either <Yes> or <No>. """
    while True:
        # asks user for input and makes it lowercase.
        user_yesno = input(question).lower()

        # checks what user entered and returns answer or asks user again.
        if user_yesno == "yes" or user_yesno == "y" or user_yesno == "ye":
            return "yes"

        elif user_yesno == "no" or user_yesno == "n":
            return "no"
        else:
            print("Please input either <yes> (y) or <no> (n). ")


def profit_goal(total_costs):
    """Calculates Profit Goal - work out profit goal and total sales required"""
    # initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:
        # ask for profit goal
        response = input("What is your profit goal (eg $500 or 50%): ")

        # check the 1st character is $
        if response[0] == "$":
            profit_type = "$"
            # get amount (everything after the $)
            amount = response[1:]

        elif response[-1] == "%":
            profit_type = "%"
            # get amt
            amount = response[:-1]

        else:
            # set response to unknown for now
            profit_type = "unknown"
            amount = response

        # number checker
        try:
            amount = float(amount)
            if amount <=0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        # check what profit type it is ($ or %)
        # if under 100, ask if %
        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no_check(f"Do you mean ${amount:.2f} ie {amount:.2f} dollars?")

            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        # if over 100, ask if $
        elif profit_type == "unknown" and amount <= 100:
            percent_type = yes_no_check(f"Do you mean {amount}%? y / n: ")

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# main routine

# loop for testing
while True:
    total_expenses = 200
    target = profit_goal(total_expenses)
    sales_target = total_expenses + target
    print(f"Profit goals target = ${target:.2f}")
    print(f"Sales target = ${sales_target:.2f}")
    print()


