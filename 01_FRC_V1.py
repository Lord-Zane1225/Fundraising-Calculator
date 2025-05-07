# Module imports go here.
import pandas
from tabulate import tabulate
from datetime import date


# Functions go here.
def make_statement(statement, decoration):
    """Emphasises headings by adding decorations
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


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


def instructions():
    print()
    make_statement("Instructions", "ℹ️")
    print('''
Instructions placeholder. 
    ''')


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


# Main routine begins here.

# Initialise variables.

# Assume we have no fixed expenses for now.
fixed_subtotal = 0
fixed_panda_string = ""


print(make_statement("Fundraising Calculator", "💰"))

print()
want_instructions = yes_no_check("Do you want to see the instructions?")
print()

if want_instructions == "yes":
    instructions()

print()

# Get product details
product_name = not_blank("Product Name: ")
quantity_made = num_check("Quantity being made: ", "integer")

# get variable expenses
print("Let's get the variable expenses... ")
variable_expenses = get_expenses("variable", quantity_made)

variable_panda_string = variable_expenses[0]
variable_subtotal = variable_expenses[1]

# ask user if they have fixed expenses and retrieve them
print()
has_fixed = yes_no_check("Do you have fixed expenses?")

if has_fixed == "yes":
    print("Getting Fixed Costs...")
    fixed_expenses = get_expenses("fixed")
    print()
    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

    # if the user has not entered any fixed expenses, set empty panda to "" so it doesn't display.
    if fixed_subtotal == 0:
        has_fixed = "no"
        fixed_panda_string = ""

total_expenses = variable_subtotal + fixed_subtotal
total_expense_string = f"Total expenses: ${total_expenses:.2f}"

# get profit goal here

# strings / output area

# get current date for heading and filename
today = date.today()

# get day month and year as separate strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# headings / strings

main_heading_string = make_statement("Fund Raising Calculator " f"({product_name}, {day}/{month}/{year})", "=")
quantity_string = f"Quantity being made: {quantity_made}"
variable_heading_string = make_statement("Variable expenses", "-")
variable_subtotal_string = f"Variable Expenses Subtotal: ${variable_subtotal:.2f}"

# set up strings if we have fixed costs
if has_fixed == "yes":
    fixed_heading_string = make_statement("Fixed Expenses", "-")
    fixed_subtotal_string = f"Fixed Expenses Subtotal: {fixed_subtotal}"

# set fixed cost strings to blank if we don't have fixed costs
else:
    fixed_heading_string = make_statement("You have no Fixed Expenses.", "-")
    fixed_subtotal_string = "Fixed Expenses Subtotal: $0.00"

# List of strings to be outputted / written to file
to_write = [main_heading_string, quantity_string,
            "\n", variable_heading_string, variable_panda_string, variable_subtotal_string,
            "\n", fixed_heading_string, fixed_panda_string, fixed_subtotal_string, total_expense_string]

print()
for item in to_write:
    print(item)


# create file to hold data (add txt extension)
file_name = f"{product_name}_{day}_{month}_{year}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")


# write the item to the file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
