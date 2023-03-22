def dentiste(text : str) -> str:
    #text = input("Parle, Roucoule, Brois la langue de Molière !!")
    voyelle = [97, 101, 105, 111, 117, 121]
    result = ""
    for i in range(len(text)):
        for y in range(len(voyelle)):
            if ord(text[i])==voyelle[y]:
                result = result + text[i]
    return result

# 97    101     105     111     117     121
print(dentiste(input("Parle, Roucoule, Brois la langue de Molière !!")))
assert dentiste("j'ai mal") == 'aia'
assert dentiste("il fait chaud") == 'iaiau'
assert dentiste("") == ''