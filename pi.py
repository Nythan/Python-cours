pi_sur_4 = 1
#moins vaut vrai si on doit soustraire me ^rochain terme de la suite
moins = True

nb_termes = int(input("saisir le nombre de termes à calculer :"))

for denominateur in range(3, nb_termes,2):
    if moins==True:
        # soustraction
        pi_sur_4 = pi_sur_4 - 1 / denominateur
    else:
        #addition
        pi_sur_4 = pi_sur_4 + 1 / denominateur
    moins = not(moins)

print("valeur approcher de PI avec",nb_termes,": ",pi_sur_4*4)