listoftouristattraction = []
while True:
    x = input("Let's go to experience!")
    match x:
        case 'add' | 'add list':
            y = input("new location:")
            listoftouristattraction.append(y)
        case 'show' | 'show list':
            for item, index in enumerate(listoftouristattraction):
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