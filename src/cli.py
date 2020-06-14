#!/usr/bin/env python
from os import path
import argparse
from src.libs.file_search_util import search_file
from src.libs.os_util import get_visible_files_from_dir, get_recursive_files_from_dir
from src.libs.color_util import ERROR_COLOR, RESET_COLOR
import sys
import colorama
"""Advanced file search program"""
'''Options -r recursive'''


CURRENT_DIR = path.abspath(path.join(path.dirname(__file__)))


def format_error_string(phrase, file, error) -> str:
    formatted_string = ERROR_COLOR + "{0}, {1}".format(phrase, file) + "\n" + str(error) + RESET_COLOR
    return formatted_string


def main():
    parser = argparse.ArgumentParser(description="Searches for files in directory for a word or phrase")
    parser.add_argument("phrase", metavar="P", type=str, help="Phrase for searching")
    parser.add_argument("-d", "--directory", metavar="D", type=str, help="Directory for the search", default=".")
    parser.add_argument("-r", "--recursive", action="store_true", help="Declares whether the folders within "
                                                                       "folders are searched"
                        )

    args = parser.parse_args()

    colorama.init()
    print("Searching with CCSearch.\n")
    if args.phrase is not None:
        if args.directory:
            selected_dir = args.directory
        else:
            selected_dir = CURRENT_DIR

        if args.recursive:
            file_list = get_recursive_files_from_dir(selected_dir)
        else:
            file_list = get_visible_files_from_dir(CURRENT_DIR)

        for file in file_list:
            try:
                sys_out = search_file(file, args.phrase)
                sys.stdout.write(sys_out)
            except UnicodeDecodeError as error:
                print(format_error_string("This file is not detectable as a readable file", file, error))
            except PermissionError as error:
                print(format_error_string("This file does not have valid permissions", file, error))

    else:
        print("Error, a phrase is required")


main()
