"""
File searching related functions.
"""
from src.libs.color_util import FILE_COLOR, RESET_COLOR, ORANGE_COLOR


def search_file(file_dir, phrase) -> str:
    """Searches through a single file given a specific phrase"""
    stdout = ""
    with open(file_dir, "r") as file_handle:
        lines = file_handle.readlines()
        for index, line in enumerate(lines):
            line = line.strip()
            if phrase in line:
                stdout += format_line(index, line, phrase)
    if len(stdout) > 0:
        stdout = format_file_name(file_dir) + stdout
    return stdout


def format_file_name(file_name):
    """Returns formatted file name with color"""
    formatted_name = FILE_COLOR + "File Name: {0}".format(file_name) + RESET_COLOR + "\n"
    return formatted_name


def format_line(line_number, line, key_word):
    """Returns a formatted line containing the search phrase"""
    key_word_index = line.find(key_word)
    first_line_part = line[0:key_word_index]
    second_line_part = ORANGE_COLOR + line[key_word_index:key_word_index+len(key_word)] + RESET_COLOR
    third_line_part = line[key_word_index+1:]
    full_line = first_line_part + second_line_part + third_line_part
    formatted_line = "Line:({0}):{1}\n".format(line_number, full_line)
    return formatted_line
