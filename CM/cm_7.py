# class
# documentation ( chaine """ ... """ juste après la déclaration)
# constructeur
# class Personne:
#   def __init__(self: 'Personne') -> None:
#       print("Appel du constructeur")
#pers va contenir une référence à un objet de type personne
# pers = Parsonne()
#
class Personne:
    """représentation d'une personne.
    Une personne est décrite par son nom et son prénom."""
    def __int__(self, nom: str = "inconnu", prenom: str = "") -> None:
        self.nom = nom
        self.prenom = prenom

    def __str__(self, ) -> str:
        return self.prenom + " " + self.nom


pers1 = Personne()
pers2 = Personne("Martin")
pers3 = Personne("Martin", "Jacques")
pers4 = Personne(prenom="Jacques", nom="Martin")

print(pers1)
print(pers2)
print(pers3)
print(pers4)
