listoftouristattraction = []
while True:
    x = input("add list,show list,edit or exit:")
    match x:
        case 'add' | 'add list':
            y = input("new location:")
            listoftouristattraction.append(y)
        case 'show' | 'show list':
            for item in listoftouristattraction:
                print(item)
        case 'exit':
            break
        case 'edit':
            z = int(input("what place you want to change?"))
            z = z-1
            listoftouristattraction[z] = input("new location:")

print("thank for using")


