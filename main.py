
while True:
    x = input("Let's go to experience!")

    if 'add'  in x or 'add list' in x:
        y = x[4:]


        with open('listoftouristattraction.txt', 'r') as file:
            listoftouristattraction = file.readlines()

        listoftouristattraction.append(y)

        with open('listoftouristattraction.txt', 'w') as file:
            file.writelines(listoftouristattraction)

    elif 'show' in x or 'show list' in x:


        with open('listoftouristattraction.txt', 'r') as file:
            listoftouristattraction = file.readlines()
        # a = [item.strip('listoftouristattraction.txt', 'r')]
        for item, index in enumerate(listoftouristattraction):
            index = index.strip('\n')
            r = f"{item + 1}.{index}"
            print(r)
    elif 'exit' in x:
        break
    elif 'edit' in x:
        z = int(x[5:])
        with open('listoftouristattraction.txt', 'r') as file:
            listoftouristattraction = file.readlines()

        z = z-1
        listoftouristattraction[z] = input("new location:") + "\n"
        with open('listoftouristattraction.txt', 'w') as file:
            file.writelines(listoftouristattraction)

    elif 'complete' in x:
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
    else:
        print("Wrong input.")
print("thank for using")