# Opérateurs

## Arithmétiques

a = 5
b = 3

# Addition
resultat = a + b

# Soustraction
resultat = a - b

# Multiplication
resultat = a * b

# Division
resultat = a / b

# Division entière
resultat = a // b

# Exposant
resultat = a ** b

# Modulo
resultat = a % b


## Comparaison

# Égalité: ==
print("a == b", a == b)

# Différence: !=
print("a != b", a != b)

# Supérieur: >
print("a > b", a > b)

# Inférieur: <
print("a < b", a < b)

# Supérieur ou égal: >=
print("a >= b", a >= b)

# Inférieur ou égal: <=
print("a <= b", a <= b)


## Logiques

# ET: and
print("True and True", True and True) # True
print("False and True", False and True) # False
print("True and False", True and False) # False
print("False and False", False and False) # False

# OU: or
print("True or True", True or True) # True
print("False or True", False or True) # True
print("True or False", True or False) # True
print("False or False", False or False) # False

# Négation: not
print("not True", not True) # False
print("not False", not False) # True

# Combinaison d'opérateurs
x = 5
y = 10
z = 15

print('(x < y) and (y < z)', (x < y) and (y < z)) # True
print('not (x < y)', not (x < y))