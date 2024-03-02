def funcCountVowels(varWord):
    varCount = 0
    for varLetter in varWord:
        if ((varLetter=="a") or (varLetter=="e") or (varLetter=="i") or (varLetter=="o") or (varLetter=="u") or 
            (varLetter=="A") or (varLetter=="E") or (varLetter=="I") or (varLetter=="O") or (varLetter=="U")):
            varCount += 1
    return varCount