# Les collections

# 1. Les listes


# Création d'une liste
fruits = ['pomme', 'banane', 'cerise']

# Ajouter un élément à la fin
fruits.append("orange")
print(fruits) # Affichage: ['pomme', 'banane', 'cerise', 'orange']

# Insérer un élément à une position spécifique
fruits.insert(1, 'kiwi')
print(fruits) # Affichage: ['pomme', 'kiwi', 'banane', 'cerise', 'orange']

# Retirer un élément
fruits.remove('banane')
print(fruits) # Affichage: ['pomme', 'kiwi', 'cerise', 'orange']

# Supprimer un élément à une position spécifique
fruits.pop()
print(fruits) # Affichage: ['pomme', 'kiwi', 'cerise']

del fruits[2]
print(fruits) # Affichage: ['pomme', 'kiwi']

# Itérer sur une liste

for fruit in fruits:
    print(fruit)
    
fruits = ['pomme', 'banane', 'cerise', 'poire', 'ananas', 'litchi']
#            0         1         2        3        4          5

print("fruits[1]", fruits[1]) # Affichage: 'banane'
print("fruits[1:3]", fruits[1:3]) # Affichage: ['banane', 'cerise']
print("fruits[:3]", fruits[:3]) # Affichage: ['pomme', 'banane', 'cerise']
print("fruits[3:]", fruits[3:]) # Affichage: ['poire', 'ananas', 'litchi']
print("fruits[::2]", fruits[::2]) # Affichage: ['pomme', 'cerise', 'ananas']
print("fruits[::-1]", fruits[::-1]) # Affichage: ['litchi', 'ananas', 'poire', 'cerise', 'banane', 'pomme']

# Copier une liste

fruits1 = fruits
fruits2 = fruits[:]
fruits3 = fruits.copy()
fruits4 = list(fruits)


print("fruits1 == fruits", fruits1 is fruits) # True
print("fruits2 == fruits", fruits2 is fruits) # False
print("fruits3 == fruits", fruits3 is fruits) # False
print("fruits4 == fruits", fruits4 is fruits) # False

# 2. Tuple

# Création d'un tuple
coordonnees = (10, 20)

# Accéder à un élément
print(coordonnees[0]) # Affichage: 10

# Les tuples sont immuables, donc aucune méthode pour ajouter ou supprimer un élément
# Vous pouvez créer un nouveau tuple par concaténation
nouvelles_coordonnees = coordonnees + (30, 40)
print(nouvelles_coordonnees) # Affichage: (10, 20, 30, 40)

# Itérer sur un tuple
for coord in nouvelles_coordonnees:
    print(coord)
    
# 3. Set

# Création d'un set
animaux = { "chat", "chien", "lapin" }

# Ajouter un élément
animaux.add('hamster')
print(animaux) # Affichage: {'chat', 'lapin', 'hamster', 'chien'}

# Ajouter plusieurs élément
animaux.update(['lion', 'renard'])
print(animaux) # Affichage: {'lapin', 'renard', 'hamster', 'chien', 'chat', 'lion'}

# Retirer un élément spécifique
animaux.remove('chat')
print(animaux) # Affichage: {'hamster', 'renard', 'lion', 'chien', 'lapin'}

# Vérifier si un élément est dans l'ensemble
print('chat' in animaux) # Affichage: False
print('lion' in animaux) # Affichage: True

# Opérations sur des ensembles
ensemble1 = {1, 2, 3}
ensemble2 = {2, 3, 4}

# Union: |
# Prendre tous les éléments des deux ensembles rassembler dans un même ensemble
print(ensemble1 | ensemble2) # Affichage: {1, 2, 3, 4}

# Intersection: &
print(ensemble1 & ensemble2) # Affichage: {2, 3}

# Différence: -
print(ensemble1 - ensemble2) # Affichage: {1}
print(ensemble2 - ensemble1) # Affichage: {4}


# 4. Dictionnaire

# Création d'un dictionnaire
etudiant = {
    "prenom": "Quentin",
    "age": 28,
    "cours": ["Angular", "C#", "Javascript"]
}

etudiant2 = dict(
    prenom = "Quentin",
    age = 28,
    cours = ["Angular", "C#", "Javascript"]
)

print(etudiant)
print(etudiant2)

# Accéder à une valeur par sa clef
print(etudiant["prenom"])
print(etudiant["age"])

etudiant["adresse"] = "123 Rue de ma rue"
print(etudiant) # Affichage: {'prenom': 'Quentin', 'age': 28, 'cours': ['Angular', 'C#', 'Javascript'], 'adresse': '123 Rue de ma rue'}

# Supprimer une paire clef-valeur
del etudiant["adresse"]
print(etudiant) # Affichage: {'prenom': 'Quentin', 'age': 28, 'cours': ['Angular', 'C#', 'Javascript']}

# Supprimer un élément
etudiant.pop("age");

# Itérer sur l'ensemble des clefs d'un dictionnaire (avec enumerate)
for index, key in enumerate(etudiant.keys()):
    print(f"{key} : {etudiant[key]}")
    
# Itérer sur l'ensemble des clefs et valeur
for key, value in etudiant.items():
    print(f"{key} : {value}")
    
# Nettoyer l'ensemble des clefs-valeurs
etudiant.clear();
print(etudiant) # Affichage: {}