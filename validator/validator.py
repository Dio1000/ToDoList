from utils.utils import *
from utils.file_functions.file_functions import *


def add_validator(argc: int, argv: list):
    if argc < 4:
        print("Too few arguments were provided for 'add'!")
        return 0

    if not os.path.isfile("lists/" + argv[2]):
        print(argv[2] + " is not a valid list!")
        return 0

    return 1


def dl_validator(argc: int, argv: list):
    if argc < 5:
        print("Too few arguments were provided for 'dl'!")
        return 0
    elif argc > 5:
        print("Too many arguments were provided for 'dl'!")
        return 0

    if not os.path.isfile("lists/" + argv[2]):
        print(argv[2] + " is not a valid list!")
        return 0

    if not valid_date(argv[4]):
        print("Deadline is not a valid date! Use format dd/MM/yyyy!")
        return 0

    return 1


def rmrow_validator(argc: int, argv: list):
    if argc < 4:
        print("Too few arguments were provided for 'rmrow'!")
        return 0
    elif argc > 4:
        print("Too many arguments were provided for 'rmrow!")
        return 0

    if not os.path.isfile("lists/" + argv[2]):
        print(argv[2] + " is not a valid list!")
        return 0

    try:
        int(argv[2])
    except:
        print("Row argument must be an integer!")
        return 0

    return 1


def rmline_validator(argc: int, argv: list):
    if argc < 4:
        print("Too few arguments were provided for 'rmline'!")
        return 0
    elif argc > 4:
        print("Too many arguments were provided for 'rmline!")
        return 0

    if not os.path.isfile("lists/" + argv[2]):
        print(argv[2] + " is not a valid list!")
        return 0

    return 1


def mklist_validator(argc: int):
    if argc < 3:
        print("Too few arguments were provided for 'mklist'!")
        return 0
    elif argc > 3:
        print("Too many arguments were provided for 'mklist!")
        return 0

    return 1


def rmlist_validator(argc: int, argv: list):
    if argc < 3:
        print("Too few arguments were provided for 'rmlist'!")
        return 0
    elif argc > 3:
        print("Too many arguments were provided for 'rmlist!")
        return 0

    if not os.path.isfile("lists/" + argv[2]):
        print(argv[2] + " is not a valid list!")
        return 0

    return 1


def show_validator(argc: int, argv: list):
    if argc < 3:
        print("Too few arguments were provided for 'show'!")
        return 0
    elif argc > 3:
        print("Too many arguments were provided for 'show!")
        return 0

    if not os.path.isfile("lists/" + argv[2]):
        print(argv[2] + " is not a valid list!")
        return 0

    return 1


def help_validator(argc: int):
    if argc < 2:
        print("Too few arguments were provided for 'help'!")
        return 0
    elif argc > 2:
        print("Too many arguments were provided for 'help!")
        return 0

    return 1
