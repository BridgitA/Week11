animals = ["cat", "goat", "dog"]
def list_o_matic(aput):
    if aput == " ":
        animals.pop()
        return aput
    elif aput in animals:
        animals.remove(aput)
        return aput 
    else:
        animals.append(aput)
        return aput       