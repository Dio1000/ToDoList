# TODO change some error messages

from utils.utils import *


def add_validator(argc: int):
    if argc <= 4:
        print("Too few arguments were provided for 'add'!")
        return 0

    return 1


def dl_validator(argc: int, argv: list):
    if argc != 5:
        print("Too few arguments were provided for 'dl'!")
        return 0

    if not valid_date(argv[4]):
        print("Deadline is not a valid date! Use format dd/MM/yyyy!")
        return 0

    return 1


def rmrow_validator(argc: int):
    if argc != 4:
        print("Too few arguments were provided for 'rmrow'!")
        return 0

    return 1


def rmline_validator(argc: int):
    if argc <= 4:
        print("Too few arguments were provided for 'rmline'!")
        return 0

    return 1


def mklist_validator(argc: int):
    if argc != 3:
        print("Too few arguments were provided for 'mklist'!")
        return 0

    return 1


def rmlist_validator(argc: int):
    if argc != 3:
        print("Too few arguments were provided for 'rmlist'!")
        return 0

    return 1


def show_validator(argc: int):
    if argc != 3:
        print("Too few arguments were provided for 'show'!")
        return 0

    return 1



