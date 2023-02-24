x = open(r'C:\Users\Admin\Downloads\members.txt', 'r')
y = x.readlines()
x.close()

add = input("Add a new member:") + '\n'
y.append(add)
x = open(r'C:\Users\Admin\Downloads\members.txt', 'w')
x.writelines(y)
x.close()
print(y)