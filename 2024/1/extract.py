filename = "data"

# Listes pour stocker les variables
list1 = []
list2 = []

# Lecture du fichier
with open(filename, "r") as f:
    for line in f:
        # Supprimer les espaces blancs au début/fin et diviser les colonnes
        part1, part2 = line.strip().split()
        # Ajouter les valeurs dans les listes
        list1.append(int(part1))
        list2.append(int(part2))

# Ordonner les listes
list1.sort()
list2.sort()

# Calcul de la différence entre chaque liste
differences = [abs(a - b) for a, b in zip(list1, list2)]

# calculer la somme totale de la liste -> resultat
results = sum(differences)

print("Le resultat est : " + str(results) + ".")

## PART 2 ##

similarity_score = 0
for item in list1:
    similarity_score += (list2.count(item) * item)

print("Le similarity score est : " + str(similarity_score) + ".")
