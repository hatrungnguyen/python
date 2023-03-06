try:
    x = float(input("Enter total value:"))
    y = float(input("Enter Value:"))

    z = y / x * 100
    print(f"That is {z}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
