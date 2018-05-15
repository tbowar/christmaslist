import os

"""
Store and retrieve names from a CSV file

Format of the file:
giver_name,spouse,receiver\n
giver_name,spouse,receiver\n
giver_name,spouse,receiver\n

"""

def add(name_file, name, spouse, receiver):
    with open(name_file, 'a') as file:
        file.write(f'{name},{spouse},{receiver}\n')


def delfile(name_file):
    os.remove(name_file)


def list_names(name_file):
    with open(name_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    try:
        return [
            {'name': line[0], 'spouse': line[1], 'receiver': line[2]}
            for line in lines
        ]
    except:
        print("Error: File does not have 3 comma separated names per line.")

def _save_all_names(name_file, names):
    with open(name_file, 'w') as file:
        for name in names:
            file.write(f"{name['name']},{name['spouse']},{name['receiver']}\n")


def name_delete(name_file, name):
    names = list_names(name_file)
    names = [person for person in names if person['name'] != name]
    _save_all_names(name_file, names)
