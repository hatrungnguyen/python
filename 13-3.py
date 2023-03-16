


def calculate(year_of_birth, current_year="2023"):

    r = int(current_year) - int(year_of_birth)
    return r


x = calculate(input("What year were you born?"))
if x <= 120:
    print("You still young")
else:
    print("How you can live so long?")