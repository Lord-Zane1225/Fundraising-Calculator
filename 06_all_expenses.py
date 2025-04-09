# functions
import pandas
from tabulate import tabulate


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


def get_expenses(exp_type, how_many=1):
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

    # how many defaults to 1
    amount = how_many
    how_much_question = "How much? $"

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
        if exp_type == "variable":

            amount = num_check(f"How many <enter for {how_many}>: ", "integer", "")

            # allows user to press <enter> to default number of items being made.
            if amount == "":
                amount = how_many

            how_much_question = "Price for one? $"

        # get price for item
        price_for_one = num_check(how_much_question, "float")

        # append to panda list
        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate cost column
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # apply currency formatting to currency columns
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    # make expense frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys', tablefmt='psql', showindex='False')
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys', tablefmt='psql', showindex='False')

    # return all items for now so we can check loop
    return expense_string, subtotal


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# main routine starts here

quantity_made = num_check("Quantity being made: ", "integer")

print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print("Getting Fixed Costs...")
fixed_expenses = get_expenses("fixed")
print()
fixed_panda = fixed_expenses[0]
fixed_subtotal = fixed_expenses[1]

# temporary output area (for easy testing)

# variable expenses output
print("=== Variable Expenses ===")
print(variable_panda)
print(f"Variable subtotal: ${variable_subtotal:.2f}")

# fixed expenses output
print("=== Fixed Expenses ===")
print(fixed_panda)
print(f"Fixed subtotal: ${fixed_subtotal:.2f}")
print()

total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses: ${total_expenses:.2f}")
