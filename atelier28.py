# Ecrire un programme en langage Python qui demande à l’utilisateur
#  de saisir son nombre entier et de lui afficher
#  si ce nombre est pair ou impair.

n = input("Entrez un nombre n : ")

# Convertir n en entier
n = int(n)
# Tester si n est pair ou non
if n % 2 == 0:
    print("Le nombre '", n, "' tapé est pair ")
else:
    print("Le nombre '", n, "' tapé est impair ")
