#!/usr/bin/python

from utils import database
from utils import create_list
import os.path
import sys


USER_CHOICE = """
Enter:
- 'a' to add a new name
- 'l' to list all names
- 'd' to delete a name

- 'n' to create a new Christmas list from old list
- 'h' for help
- 'q' to quit

Your choice: """

HELP = """
Christmas list program

The Christmas list file format is:
giver_name,spouse,receiver\n
giver_name,spouse,receiver\n
giver_name,spouse,receiver\n

For example:
Tom,Mary,Joe
or
Tom, Mary, Joe

- Names must be unique.
- Each line must contain 3 "names", separated by commas.
- If there is no spouse, use a character (such as x) to designate spouse,
  as long as it is not used as a member's name.
- Spaces may be used between names.
- The file name may be specified on the command line, i.e.:
        christmaslist.py namelist.txt
"""


def menu():
    filename = get_filename()

    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_name(filename)
        elif user_input == 'l':
            list_names(filename)
        elif user_input == 'd':
            prompt_delete_name(filename)
        elif user_input == 'n':
            filename = create_new_list(filename)
        elif user_input == 'h':
            help()
        else:
            print('Unknown command, please try again.')

        user_input = input(USER_CHOICE)


def prompt_add_name(file_name):
    name = str(input('Giver\'s Name: '))
    spouse = str(input('Spouse: '))
    receiver = str(input('Last year gift receiver: '))
    database.add(file_name, name, spouse, receiver)


def list_names(file_name):
    names = database.list_names(file_name)
    if names:
        for name in names:
            print(f"{name['name']}, {name['spouse']}, {name['receiver']}")


def prompt_delete_name(file_name):
    name_del = str(input('Enter a name to delete: '))
    database.name_delete(file_name, name_del)


def prompt_new_file_name():
    filename = str(input('Enter NEW Christmas list filename: '))
    while os.path.isfile(filename):
        yn = input(f'File name: {filename} exists, are you sure you want to overwrite? y/N ')
        if yn.lower() == 'y':
            database.delfile(filename)
        else:
            filename = str(input('Enter NEW Christmas list filename: '))
    return filename


def prompt_old_file_name():
    filename = str(input('Enter last year\'s Christmas list filename: '))
    return filename


def help_screen():
    print(HELP)


def create_new_list(file_name):
    newname = prompt_new_file_name()
    create_list.new_list(file_name, newname)
    print(f'{newname} is now the current file.')
    return newname


def get_filename():
    if len(sys.argv) < 2:
        filename = prompt_old_file_name()
    else:
        filename = sys.argv[1]
    while not os.path.isfile(filename):
        print(f'File name: {filename} not found.')
        filename = prompt_old_file_name()
    return filename


menu()