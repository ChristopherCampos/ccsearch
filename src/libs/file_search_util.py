"""
File searching related functions.
"""


def search_file(file_dir, phrase) -> str:
    """Searches through a single file given a specific phrase"""
    stdout = ""
    with open(file_dir, "r") as fhandle:
        lines = fhandle.readlines()
        for index, line in enumerate(lines):
            line = line.strip()
            if phrase in line:
                stdout += ("Line:({0}): {1}\n".format(index, line))
    if len(stdout) > 0:
        stdout = "File Name: {0}\n".format(file_dir) + stdout
    return stdout

