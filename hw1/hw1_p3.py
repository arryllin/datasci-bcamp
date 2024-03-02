varCount = 1
while varCount <= 20:
    print(str(varCount) + " is ", end = "")
    if (varCount%2) == 0:
        print("even")
    else:
        print("odd")
    varCount += 1