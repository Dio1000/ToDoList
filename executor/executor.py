from ui.ui import *
from utils.file_functions.file_functions import *
from utils.utils import *
from validator.validator import *


def execute_program(argc: int, argv: list):
    if argc <= 1:
        print("Too few arguments were provided!")

    argument = argv[1]

    if argument == "add" and add_validator(argc):
        execute_add(argv)
    if argument == "dl" and dl_validator(argc, argv):
        execute_dl(argv)
    if argument == "rmrow" and rmrow_validator(argc):
        execute_rmrow(argv)
    if argument == "rmline" and rmline_validator(argc):
        execute_rmline(argv)
    if argument == "mklist" and mklist_validator(argc):
        execute_mklist(argv)
    if argument == "rmlist" and rmlist_validator(argc):
        execute_rmlist(argv)
    if argument == "show" and show_validator(argc):
        execute_show(argv)


def execute_add(argv: list):
    file_path = "lists/" + argv[2]
    argument = get_argument(argv, 3)

    write_to_file(file_path, argument)
    return 1


def execute_dl(argv: list):
    file_path = "lists/" + argv[2]
    row = int(argv[3])
    new_line = argv[4]

    add_deadline_to_row(file_path, row, new_line)
    return 1


def execute_rmrow(argv: list):
    file_path = "lists/" + argv[2]
    argument = argv[3]

    remove_row_from_file(file_path, int(argument))


def execute_rmline(argv: list):
    file_path = "lists/" + argv[2]
    argument = get_argument(argv, 3)

    remove_line_from_file(file_path, argument)


def execute_mklist(argv: list):
    file_path = "lists/" + argv[2]

    create_file(file_path)


def execute_rmlist(argv: list):
    file_path = "lists/" + argv[2]

    remove_file(file_path)


def execute_show(argv: list):
    file_path = "lists/" + argv[2]

    display_tasks(file_path, argv[2])
