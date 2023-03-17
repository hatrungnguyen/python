def list_place(filepath="listoftouristattraction.txt"):
    """ Read a text file and return a place"""
    with open(filepath, 'r') as file:
        readplace = file.readlines()
    return readplace


def write_place(places, filepath="listoftouristattraction.txt"):
    """" Write a place in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(places)
