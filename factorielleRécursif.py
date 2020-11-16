#!/usr/bin/python3
# coding: utf-8


# Le nombre d'appels récursifs possibles dépend de la valeur de n.
def factorial(n):
  if (n == 1):
    return 1
  # else: // remplace la dernière ligne de la fonction.
  #  return n * factorial (n-1)
  return n * factorial(n-1)


try:
  n = int(input("Entrez un nombre dont on veut la factorielle : "))
  print("Sa factorielle est :", factorial(n))
except:
  print(“Veuillez saisir un nombre.”)
)e


----------------------------------------------------------------------- Résultat ---------------------------------------------------------------------------
Entrez un nombre dont on veut la factorielle : 5
Sa factorielle est : 120
~                                                                        
Sa
~