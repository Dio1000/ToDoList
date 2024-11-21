from ui.ui import *
from validator.validator import *


def execute_program(argc: int, argv: list):
    if argc <= 1:
        print("Too few arguments were provided!")
        return 0

    argument = argv[1].lower()

    if argument == "add" and add_validator(argc, argv):
        execute_add(argv)
    if argument == "dl" and dl_validator(argc, argv):
        execute_dl(argv)
    if argument == "rmrow" and rmrow_validator(argc, argv):
        execute_rmrow(argv)
    if argument == "rmline" and rmline_validator(argc, argv):
        execute_rmline(argv)
    if argument == "mklist" and mklist_validator(argc):
        execute_mklist(argv)
    if argument == "rmlist" and rmlist_validator(argc, argv):
        execute_rmlist(argv)
    if argument == "show" and show_validator(argc, argv):
        execute_show(argv)
    if argument == "help" and help_validator(argc):
        execute_help()


def execute_add(argv: list):
    file_path = "lists/" + argv[2]
    argument = get_argument(argv, 3)
    write_to_file(file_path, argument)


def execute_dl(argv: list):
    file_path = "lists/" + argv[2]
    row = int(argv[3])
    new_line = argv[4]
    add_deadline_to_row(file_path, row, new_line)


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


def execute_help():
    display_help()