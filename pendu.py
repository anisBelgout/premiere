import random
random.randint(0,22740)

fichier = open('fichier.md','r')
chaine = fichier.readline()
fichier.close()
print(chaine)



from random import choice
from unidecode import unidecode

def pendu ():
    f = open('fichier.md', 'r' , encoding = 'utf8')
    contenu = f.readlines()
    return unidecode( choice(contenu) ).upper().replace('\n','')
def underscore(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '          
    return r[:-1]
def saisie():
    lettre = input('Choissisez une lettre : ')
    if len( lettre ) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    else:
        return lettre.upper()
lettres_deja_proposees = []
mot_a_deviner = pendu()
affichage = underscore( mot_a_deviner )
nb_erreurs = 0
while '_' in affichage and nb_erreurs < 11:
    lettre = saisie()
    if lettre not in lettres_deja_proposees:
        lettres_deja_proposees += [ lettre ]
    if lettre not in mot_a_deviner:
        nb_erreurs += 1
        affichage = underscore( mot_a_deviner , lettres_deja_proposees )
    print( 'Choissisez une lettre :' , affichage *9, 'Il vous reste' , 11-nb_erreurs ,'chances')
print("fin du game")
