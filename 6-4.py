filename = ['1.txt', '2.txt', '3.txt']
for x in filename:
    file = open(x, 'w')
    file.write("Hello")
    file.close
