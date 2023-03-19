FILEPATH = "listoftouristattraction.txt"


def list_place(filepath=FILEPATH):
    """ Read a text file and return a place"""
    with open(filepath, 'r') as file:
        readplace = file.readlines()
    return readplace


def write_place(places, filepath=FILEPATH):
    """" Write a place in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(places)
