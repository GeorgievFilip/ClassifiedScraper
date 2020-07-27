import random
import re
import os
#
# get a single random item from a list
def random_choice(a_list):
    if a_list is None:
        pass
    elif a_list == []:
        pass
    else:
        return random.choice(a_list)

# transform string-like integer into an integer 
def return_int(string):
    if isinstance(string, int):
        return string
    else:
        return int(string)

# get a rounded number from an integer by a given denominator
def get_round(integer, denominator):
    return int(-(-integer // denominator))

# extracts integers from a string
def extract_number(string):
    if isinstance(string, int):
        return string
    elif isinstance(string, str):
        return int(re.sub("[^0-9]", "", string))
    else:
        return None

# reads txt file and returns only the unique items in the file
def txt_read(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    lines = list(set(lines))
    f.close()
    return lines

# split a string
def split_string_at(string, split_string, num = None):
    num = None if num is None else num
    if num is None:
        return string.split(split_string)
    else:
        return string.split(split_string)[num]

# make a dictionary
def make_directory(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)