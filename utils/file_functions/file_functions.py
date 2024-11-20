import os


def create_file(file_path: str):
    if os.path.isfile(file_path):
        return 0

    with open(file_path, "w"):
        pass
    return 1


def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)


def write_to_file(file_path: str, line: str):
    with open(file_path, "a") as write_file:
        line = line.strip(" ")
        write_file.write(line + ",NULL\n")

    write_file.close()


def remove_row_from_file(file_path: str, row: int):
    with open(file_path, "r") as read_file:
        lines = read_file.readlines()

    if 1 <= row <= len(lines):
        del lines[row - 1]
    else:
        return 0

    with open(file_path, "w") as write_file:
        write_file.writelines(lines)

    return 1


def add_deadline_to_row(file_path: str, row: int, new_line: str):
    with open(file_path, "r") as read_file:
        lines = read_file.readlines()

    if 1 <= row <= len(lines):
        lines[row - 1] = lines[row - 1].strip("\n")
        parts = lines[row - 1].split(",")
        parts[1] = new_line
        lines[row - 1] = parts[0] + "," + parts[1] + "\n"
    else:
        return 0

    with open(file_path, "w") as write_file:
        write_file.writelines(lines)

    return 1


def remove_line_from_file(file_path: str, line: str):
    lines = []
    line = line.strip(" ")

    with open(file_path, "r") as read_file:
        for line_ in read_file:
            lines.append(line_.strip("\n").strip(" "))

    try:
        lines.remove(line)
        with open(file_path, "w") as write_file:
            write_file.writelines(lines)

        return 1

    except ValueError:
        return 0


def get_lines_from_file(file_path: str):
    with open(file_path, "r") as read_file:
        lines = read_file.readlines()

    return lines
