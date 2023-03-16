
def calculate(year_of_birth, current_year="2023"):

    r = int(current_year) - int(year_of_birth)
    return r


print(calculate(input("What year were you born?")))