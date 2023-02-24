menu = ["tam rice", "phở", "bánh mì"]
menu.sort()
for x, y in enumerate(menu):
    r = f"{x + 1}.{y}"
    print(r)