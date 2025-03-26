# functions go here

def make_statement(statement, decoration):
    """Emphasises headings by adding decorations
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list, letter_amt_req):
    """Checks that users enter the full world or a chosen amount of letters of a word from a list of valid responses. """

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item

            elif response == item[:letter_amt_req]:
                return item

        print(f"Please choose an answer from {valid_ans_list}. ")


def instructions():
    print()
    make_statement("Instructions", "ℹ️")
    print('''
Instructions placeholder. 
    ''')


# main routine
yes_no_tuple = ("yes", "no")

want_instructions = string_check("Do you want to read the instructions? ", yes_no_tuple, 1)
if want_instructions == "yes":
    instructions()
