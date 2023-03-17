def list_place(filepath="listoftouristattraction.txt"):
    """ Read a text file and return a place"""
    with open(filepath, 'r') as file:
        readplace = file.readlines()
    return readplace


def write_place(places, filepath="listoftouristattraction.txt"):
    """" Write a place in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(listoftouristattraction)



while True:
    x = input("Let's go to experience!")

    if x.startswith('add'):

        y = x[4:]


        listoftouristattraction = list_place()

        listoftouristattraction.append(y + '\n')


        write_place(listoftouristattraction)

    elif x.startswith('show' or 'show list'):


        listoftouristattraction = list_place()
        # a = [item.strip('listoftouristattraction.txt', 'r')]
        for index, item in enumerate(listoftouristattraction):
            item = item.strip('\n')
            r = f"{index + 1}.{item}"
            print(r)
    elif x.startswith('exit'):
        break
    elif x.startswith('edit'):
        try:
            z = int(x[5:])
            listoftouristattraction = list_place()

            z = z-1
            listoftouristattraction[z] = input("new location:") + "\n"
            write_place(listoftouristattraction)
        except ValueError:
            print("Wrong input")
            continue


    elif x.startswith('complete'):
        try:
            z = int(x[9:])
            listoftouristattraction = list_place()

            z = z - 1
            placeremove = listoftouristattraction[z].strip('\n')
            listoftouristattraction.pop(z)
            write_place(listoftouristattraction)
            message = f"{placeremove} has been deleted"
            print(message)
        except IndexError:
            print("You don't have that much place in your list")
            continue
        except ValueError:
            print("You must enter a number.")
            continue
    else:
        print("Wrong input.")
print("Thank for using")