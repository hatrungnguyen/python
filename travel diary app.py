
while True:
    x = input("Let's go to experience!")

    if x.startswith('add' or 'add list'):

        y = x[4:]


        with open('listoftouristattraction.txt', 'r') as file:
            listoftouristattraction = file.readlines()

        listoftouristattraction.append(y + '\n')


        with open('listoftouristattraction.txt', 'w') as file:
            file.writelines(listoftouristattraction)

    elif x.startswith('show' or 'show list'):


        with open('listoftouristattraction.txt', 'r') as file:
            listoftouristattraction = file.readlines()
        # a = [item.strip('listoftouristattraction.txt', 'r')]
        for item, index in enumerate(listoftouristattraction):
            index = index.strip('\n')
            r = f"{item + 1}.{index}"
            print(r)
    elif x.startswith('exit'):
        break
    elif x.startswith('edit'):
        try:
            z = int(x[5:])
            with open('listoftouristattraction.txt', 'r') as file:
                listoftouristattraction = file.readlines()

            z = z-1
            listoftouristattraction[z] = input("new location:") + "\n"
            with open('listoftouristattraction.txt', 'w') as file:
                file.writelines(listoftouristattraction)
        except ValueError:
            print("Wrong input")
            continue


    elif x.startswith('complete'):
        try:
            z = int(x[9:])
            with open('listoftouristattraction.txt', 'r') as file:
                listoftouristattraction = file.readlines()

            z = z - 1
            placeremove = listoftouristattraction[z].strip('\n')
            listoftouristattraction.pop(z)
            with open('listoftouristattraction.txt', 'w') as file:
                file.writelines(listoftouristattraction)
            message = f"{placeremove} has been deleted"
            print(message)
        except IndexError:
            print("You don't have that much place in your list")
            continue
    else:
        print("Wrong input.")
print("thank for using")