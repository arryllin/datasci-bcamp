listAnimals = ["tiger", "elephant", "monkey", "zebra", "panther"]

for varAnimal in listAnimals:
    for varLetter in varAnimal:
        print(chr((ord(varLetter) - 32)), end = "") # converts to uppercase
    print() # linebreak