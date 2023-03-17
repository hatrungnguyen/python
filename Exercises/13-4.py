def number(number_of_name):
    item = number_of_name.split(',')
    return len(item)
names = input("Enter name separated by commas (no spaces):")
print(number(names))