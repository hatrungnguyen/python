xpassword = input("Your password:")
def strength(password):
    result = {}
    if len(password) >= 8:
        result["a"] = True
    else:
        result["a"] = False
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["b"] = digit
    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["c"] = uppercase
    if all(result.values()) == True:
        return "Strong password"
    else:
        return "Weak password"
print(strength(xpassword))
