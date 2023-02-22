filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    x = item.title()
    y = f"{index}-{x}.txt"
    print(y)