"""
a= input("Entrer un prmeire nombre : ")
b=input("Entrer un deuxième nombre : ")
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a)+int(b)}")
"""
'''
age = 15
if age >= 18 :
    print("Vous etes majeur !")
else :
    print("vous etes mineur") 
'''
'''
utilisateur = "admin"
mot_de_passe = "reda"
if utilisateur == "admin" and mot_de_passe == "admin":
   print("accès autorisé ! ")
else:
   print("accès refusé !")
'''
'''
import random
r = random.randint(0 , 1)
print(r)

s = random.uniform(0 , 1)
print(s)

b= random.randrange(0 , 100 , 5 )
print(b)
'''
'''
import os 
chemin = "C:/Users/bouffi1u/Downloads/projet Python"
dossier = os.path.join(chemin , "test")
os.makedirs(dossier)
if os.path.exists(dossier):
 os.removedirs(dossier)
print(dossier)
'''
'''
liste =[1 ,2 , 3, 4 , 5]
liste.extend([11 , 12 , 14])
liste.remove(11)
print(liste[0:-1:2])
'''
'''
employes = ["said","reda","belaid","hamza"]
result = "\t".join(employes)
employes.reverse()
employes.sort()
employes.pop(0)
cousres = "riz , pomme  , lait"
cousres = cousres.split(",")
if "said" in employes:
    print("bonjour said , bienvenu parmi nous")
print(cousres)

print(result)
print(employes[0] [0:2])
employes.append("tarik")
print(employes)

mdp = input("entrez un mot de passe (min 8 caractères ) :")
mdp_trop_court = "votre mot de passe est trop court"

if len(mdp) == 0 :
    print(mdp_trop_court.upper())
elif len(mdp)<8:
    print(mdp_trop_court.capitalize())
elif mdp.isdigit():
    print("votre mot de passe contient des nombres")
else:
    print("inscrption terminé")
'''
'''
for i in [0,1,2,4,5]:
    print(i)

for i in range(10):
    print("Bonjour")


continuer = "o"
while continuer == "o":
    print("On continue ...")
    continuer = input("Vous voulez contiuez ? o/n")    


import time
while True :
    print(" Sauvgarde en cours ....")
    time.sleep(0.5)
'''

'''

liste = [ "1" , "4" , "Paul" ,"3"]
for element in liste:
    if element.isdigit():
        continue# contiue la boucle si il trouve un nombre et affiche finalament la chain de caratère 
    print(element)
liste = [ "1" , "4" , "Paul" ,"3"]
for element in liste:
    if element.isdigit():
        break #arreter la boucle et n'affche rien si il trouve un nombre 
    print(element)
'''
'''
liste = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
nombres_positives = []
for i in liste:
    if i > 0:
        nombres_positives.append(i)
print(nombres_positives)
'''
nombres = range(10)
nombres_inverses = []
for i in nombres:
    if i % 2 == 0 :
        nombres_inverses.append(i)
    else:
        nombres_inverses.append(-i)
print(nombres_inverses)
