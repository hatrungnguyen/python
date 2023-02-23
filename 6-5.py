x = [r'C:\Users\Admin\Downloads\a.txt', r'C:\Users\Admin\Downloads\b.txt', r'C:\Users\Admin\Downloads\c.txt']
for file in x:
    read = open(file, 'r')
    y =read.read()
    read.close()
    print(y)