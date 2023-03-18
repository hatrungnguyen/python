freezing_point = 0
boiling_point = 100



def t(x):
    if x <= freezing_point:
        return "soild"
    elif freezing_point < x < boiling_point:
        return "liquid"
    else:
        return "gas"
