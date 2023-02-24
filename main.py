
while True:
    x = input("Let's go to experience!")
    match x:
        case 'add' | 'add list':
            y = input("new location:") + "\n"
            file = open('listoftouristattraction.txt', 'r')
            listoftouristattraction = file.readlines()
            file.close()
            listoftouristattraction.append(y)
            file = open('listoftouristattraction.txt', 'w')
            file.writelines(listoftouristattraction)
            file.close()

        case 'show' | 'show list':

            file = open('listoftouristattraction.txt', 'r')
            listoftouristattraction = file.readlines()
            file.close()
            # a = [item.strip('\n') for item in listoftouristattraction]
            for item, index in enumerate(listoftouristattraction):
                index = index.strip('\n')
                r = f"{item + 1}.{index}"
                print(r)
        case 'exit':
            break
        case 'edit':
            z = int(input("what place you want to change?"))
            z = z-1
            listoftouristattraction[z] = input("new location:")
        case 'complete':
            z = int(input("what place you want to complete?"))
            z = z - 1
            listoftouristattraction.pop(z)
print("thank for using")