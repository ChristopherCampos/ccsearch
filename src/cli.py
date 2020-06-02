#!/usr/bin/env python
from os import path
import argparse
from src.libs.file_search_util import search_file
from src.libs.os_util import get_visible_files_from_dir, get_recursive_files_from_dir
import sys
"""Advanced file search program"""
'''Options -r recursive'''


CURRENT_DIR = path.abspath(path.join(path.dirname(__file__)))


def main():
    parser = argparse.ArgumentParser(description="Searches for files in directory for a word or phrase")
    parser.add_argument("phrase", metavar="P", type=str, help="Phrase for searching")
    parser.add_argument("-d", "--directory", metavar="D", type=str, help="Directory for the search", default=".")
    parser.add_argument("-r", "--recursive", action= "store_true",help="Declares whether the folders within "
                                "folders are searched")
    args = parser.parse_args()

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
                print("This file is not detectable as a readable file, {}.\n".format(file), error)
            except PermissionError as error:
                print("This file does not have valid permissions, {}\n".format(file), error)

    else:
        print("Error, a phrase is required")


main()
