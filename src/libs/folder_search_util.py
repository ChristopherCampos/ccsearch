"""
Folder searching related functions.
"""
from src.libs.os_util import get_visible_files_from_dir, get_recursive_files_from_dir
from src.libs.file_search_util import search_file
import sys


def search_directory(dir_address, phrase):
    """Searches a single directory and returns the lines found in the file"""
    file_list = get_visible_files_from_dir(dir_address)
    for file in file_list:
        sysout = search_file(file, phrase)
        sys.stdout.write(sysout)


def search_directory_recursively(dir_address, phrase):
    """Searches through a directory recursively"""
    component_list = get_visible_files_from_dir(dir_address)
    for component in component_list:
        pass
