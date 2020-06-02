"""
OS related functions.
"""

from os import listdir, path, walk


def get_visible_files_from_dir(directory, hidden=False) -> list:
    """Gets a list of all files in a directory"""
    file_list = list()
    for file_dir in listdir(directory):
        if path.isfile(file_dir):
            file_list.append(file_dir)
    return file_list


def get_recursive_files_from_dir(directory) -> list:
    total = list()
    for dir_path, _, file_names in walk(directory):
        print(dir_path, _, file_names)
        for file_name in file_names:
            total.append(path.join(dir_path, file_name))
    return total
