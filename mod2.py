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
while animals:
    print("look at all animals: ", animals)
    aput = input("Enter the name of an animal:")
    if aput == "quit":
        print("Goodbye!")
        break 
    else:
        list_o_matic(aput)              