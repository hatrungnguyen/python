while True:
    with open("bluff.txt", 'r') as file:
        side = file.readlines()
    coin = input("Thorw the coin and head or tail here: ?") + "\n"
    side.append(coin)
    with open("bluff.txt", 'w') as file:
        file.writelines(side)
    head = side.count("head\n")

    percent = head / len(side) * 100
    print(f"head:{percent}%")
