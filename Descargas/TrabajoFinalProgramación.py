def es_letra(entrada:str)->bool:
    abecedario_1 = ["a","b","c","d","e","f","g","h","i","j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    abecedario_2 = ["A","B","C","D","E","F","G","H","I","J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    devolver = True
    for letra in entrada:
        if letra not in abecedario_1 and letra not in abecedario_2:
            devolver = False
    return devolver

assert es_letra ("hola") == True
assert es_letra ("HOLA") == True
assert es_letra ("12") == False
assert es_letra ("Que") == True
