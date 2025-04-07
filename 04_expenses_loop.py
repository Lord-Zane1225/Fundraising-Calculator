# functions

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


def get_expenses(exp_type):
    """Gets variable / fixed expenses and outputs panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_items = []

    # expenses dictionary
    # loop to get expenses
    while True:
        item_name = not_blank("Item name: ")

        # checks users enter at least one variable expense
        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
            print("Oops - You have not entered anything. ")

        elif item_name == "xxx":
            break

        # add to list
        all_items.append(item_name)

    # return all items for now so we can check loop
    return all_items


# main routine
print("Getting Variable Costs...")
variable_expenses = get_expenses("variable")
num_variable = len(variable_expenses)
print(f"You have entered {num_variable} items. ")

