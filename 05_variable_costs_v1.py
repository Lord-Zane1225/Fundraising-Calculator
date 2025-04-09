# functions
import pandas


def num_check(question, num_type="float", exit_code=None):
    """Checks that users enter an integer / float more than 0 (or optional exit code)"""
    if num_type == "float":
        error = "Oops - Please enter a number more than 0"
        change_to = float
    else:
        error = "Oops - Please enter an integer (no decimals) more than 0"
        change_to = int

    while True:
        response = input(question).lower()

        # checks for the exit code
        if response == exit_code:
            return response
        try:
            # check response is an integer and is more than 0
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def get_expenses(exp_type, how_many):
    """Gets variable / fixed expenses and outputs panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    # default amount to 1 for fixed expenses and to avoid PEP 8 error for variable expenses.
    amount = 1

    # loop to get expenses
    while True:

        item_name = not_blank("Item name: ")

        # checks users enter at least one variable expense
        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
            print("Oops - You have not entered anything. You need at least one item. ")
            continue

        elif item_name == "xxx":
            break

        # add to list

        # get item amount <enter> defaults to number of products being made.

        amount = num_check(f"How many <enter for {how_many}>: ", "integer", "")

        if amount == "":
            amount = how_many

        cost = num_check("Price for one? ", "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(cost)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate row cost
    expense_frame['Cost']= expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # return all items for now so we can check loop
    return expense_frame, subtotal


# main routine starts here

quantity_made = num_check("Quantity being made: ", "integer")

print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()

variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print(variable_panda)
print(variable_subtotal)
