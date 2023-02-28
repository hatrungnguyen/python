
while True:
    x = input("Let's go to experience!")
    match x:
        case 'add' | 'add list':
            y = input("new location:") + "\n"

            with open('listoftouristattraction.txt', 'r') as file:
                listoftouristattraction = file.readlines()

            listoftouristattraction.append(y)

            with open('listoftouristattraction.txt', 'w') as file:
                file.writelines(listoftouristattraction)

        case 'show' | 'show list':


            with open('listoftouristattraction.txt', 'r') as file:
                listoftouristattraction = file.readlines()
            # a = [item.strip('listoftouristattraction.txt', 'r')]
            for item, index in enumerate(listoftouristattraction):
                index = index.strip('\n')
                r = f"{item + 1}.{index}"
                print(r)
        case 'exit':
            break
        case 'edit':
            z = int(input("what place you want to change?"))
            with open('listoftouristattraction.txt', 'r') as file:
                listoftouristattraction = file.readlines()

            z = z-1
            listoftouristattraction[z] = input("new location:") + "\n"
            with open('listoftouristattraction.txt', 'w') as file:
                file.writelines(listoftouristattraction)

        case 'complete':
            z = int(input("what place you want to complete?"))
            with open('listoftouristattraction.txt', 'r') as file:
                listoftouristattraction = file.readlines()

            z = z - 1
            placeremove = listoftouristattraction[z].strip('\n')
            listoftouristattraction.pop(z)
            with open('listoftouristattraction.txt', 'w') as file:
                file.writelines(listoftouristattraction)
            message = f"{placeremove} has been deleted"
            print(message)
print("thank for using")