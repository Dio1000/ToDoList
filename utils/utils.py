def get_argument(argv: list, start: int):
    argument = ""
    for index in range(start, len(argv)):
        argument += argv[index] + " "

    return argument


def valid_date_integer(num: str, size: int):
    if len(num) < 1 or len(num) > size:
        return 0

    for digit in num:
        if '0' > digit or '9' < digit:
            return 0

    return 1


def valid_date(date: str):
    if len(date) == 0:
        return 0

    tokens = date.split("/")
    if len(tokens) < 3:
        return 0

    day = tokens[0]
    month = tokens[1]
    year = tokens[2]

    return valid_date_integer(day, 2) and valid_date_integer(month, 2) and valid_date_integer(year, 4)


