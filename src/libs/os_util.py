"""
OS related functions.
"""

from os import listdir, path


def get_visible_files_from_dir(directory) -> list:
    """Gets a list of all files in a directory"""
    file_list = list()
    for current_directory in listdir(directory):
        if path.isfile(current_directory):
            file_list.append(current_directory)
    return file_list

#def _get_files