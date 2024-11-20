import string

from utils.file_functions.file_functions import get_lines_from_file

offset = 5
max_length = 0


def display_tasks(file_path: string, list_name: string):
    global max_length
    lines = get_lines_from_file(file_path)

    if len(lines) == 0:
        print("No tasks to display currently!")

    for line in lines:
        if len(line) > max_length:
            max_length = len(line)

    display_empty_row(max_length)
    display_in_middle(max_length, list_name)
    display_empty_row(max_length)

    display_line(max_length, "Task", "Deadline")
    display_empty_row(max_length)

    for line in lines:
        task = line.split(",")[0].strip("\n")
        deadline = line.split(",")[1].strip("\n")
        display_line(max_length, task, deadline)

    display_empty_row(max_length)
    

def display_empty_row(length: int):
    print("+" + "-" * (offset * 2 + length - 2) + "+")


def display_in_middle(length: int, line: str):
    formula = int((offset * 2 + length - 3) / 2)
    print("|" + " " * formula + line + " " * formula + "|")


def display_line(length: int, line1: str, line2: str):
    formula = int((offset * 2 + length - 3) / 4)
    display1 = "|" + " " * formula + line1 + " " * formula + "|"
    display2 = " " * formula + line2 + " " * formula + "|"

    print(display1 + display2)



