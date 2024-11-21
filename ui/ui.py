import string

from utils.file_functions.file_functions import get_lines_from_file

offset = 5
max_length = 0
max_task = 0
max_date = 0


def display_help():
    display_tasks("lists/Help", "Help")


def display_tasks(file_path: string, list_name: string):
    global max_length, max_task, max_date
    lines = get_lines_from_file(file_path)

    if len(lines) == 0:
        print("No tasks to display currently!")

    for line in lines:
        if len(line) > max_length:
            max_length = len(line) + offset

            task = line.split(",")[0]
            if len(task) > max_task:
                max_task = len(task)

            date = line.split(",")[1]
            if len(date) > max_date:
                max_date = len(date)

    display_empty_row(max_length)
    display_in_middle(max_length, list_name)
    display_empty_row(max_length)

    for line in lines:
        task = line.split(",")[0].strip("\n")
        date = line.split(",")[1].strip("\n")
        if date == "NULL":
            date = "Not set."

        display_line(task, max_task, date, max_date)

    display_empty_row(max_length)
    

def display_empty_row(length: int):
    print("+" + "-" * (offset * 2 + length) + "+")


def display_in_middle(length: int, line: str):
    formula = 2 + (offset * 2 + length)
    display = "|"

    index = 1
    while index < (formula - offset) / 2:
        display += " "
        index += 1
    display += line

    while index < formula - len(line) - 1:
        display += " "
        index += 1
    display += "|"

    print(display)


def display_line(line1: str, length1: int, line2: str, length2: int):
    total_length = 5 + length1 + length2 + 2 * offset
    remaining_length = 2 + 2 * offset + max_length - total_length

    display1 = "| " + line1
    index = len(display1) - 1
    while index <= 2 + length1 + offset + remaining_length / 2:
        display1 += " "
        index += 1

    display2 = " | " + line2
    index += len(display2)
    while index <= total_length:
        display2 += " "
        index += 1
    display2 += "|"

    print(display1 + display2)



