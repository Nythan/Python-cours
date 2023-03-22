def limite_amplitude(x:int, min:int, max:int) ->int:
    if x>max:
        x =max
    elif x<min:
        x=min
    return x

def ecrete(tab, min:int,max:int) -> list:
    result = []
    for i in range(len(tab)):
        result.append(limite_amplitude(tab[i],min,max))
    return result


assert limite_amplitude(50,-150,150) == 50
assert limite_amplitude(-200,-150,150) == -150
assert limite_amplitude(200,-150,150) == 150

assert ecrete([],-150,150) == []

valeurs = [30,5,-2,15,12]
attendu = [30,5,-2,15,12]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur, la fonction a renvoyé {resultat}"

valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
attendu = [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur, la fonction a renvoyé {resultat}"