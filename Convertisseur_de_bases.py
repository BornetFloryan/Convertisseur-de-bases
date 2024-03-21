#Programme division euclidienne de la base 10 à la base finale.
def base_final(n,f):
    if n==0:
        return '0' 
    else:
        re=''
        while n!=0:
            r=n%f #Calcul du reste de la division.
            if r<10:
                re=str(r)+re #Additionne le reste par le résultat.
            else:
                re=chr(r+55)+re #Convertit le nombre au caractère correspondant dans la table Ascii.
            n//=f #Division euclidienne.
        return re 
#Entrées.
nombre=str(input("Donnez nombre initiale ne dépassant pas 20 chiffres : "))#Nombre à convertir en base 10 convertit en chaine.
nombre=nombre.upper() #Force les charactères à être en majuscule.
if len(nombre)>20: #Vérifie si le nombre ne dépasse pas 20 charactères.
    print("Le nombre ne doit pas dépasser 20 chiffres !")
    quit()
elif nombre=='':
    print("Aucune valeur n'a été spécifiée")
    quit()
elif nombre<='0':
    print("Le nombre ne doit pas être inférieur à 1 !")
    quit()
try:  
    base_i=int(input("Donner la base initiale différente de 2, 10 ou 16 : ")) #Base initiale.
except:
    print("Impossible de mettre un charactère pour une base !")
    quit()
if base_i<2 or base_i>20: #Vérifie si le nombre défini n'est pas inférieur ou supérieur à 20.
    print("Veuillez saisir une base initiale qui n'est pas inférieur à 2 ou supérieur à 20 !")
    quit()
elif base_i==2 or base_i==10 or base_i==16: #Vérifie si le nombre défini ne correspond pas à 2, 10 ou 20.
    print("Les bases 2, 10 et 16 ne sont pas disponible à la conversion !")
    quit()
try:
    base_f=int(input("Donnez la base finale différente de la base initiale et de 2, 10 ou 16 : ")) #Base finale.
except:
    print("Impossible de mettre un charactère pour une base !")
    quit()
if base_f<2 or base_f>20: #Vérifie si le nombre défini n'est pas inférieur ou supérieur à 20.
    print("Veuillez saisir une base finale qui n'est pas inférieur à 2 ou supérieur à 20 !")
    quit()
elif base_f==2 or base_f==10 or base_f==16: #Vérifie si le nombre défini ne correspond pas à 2, 10 ou 20.
    print("Les bases 2, 10 et 16 ne sont pas disponible à la conversion !")
elif base_f==base_i: #Vérifie si la base final ne correspond pas avec la base initiale.
    print("Veuillez choisir une base différente de l'initiale !")
    quit()

u=1
p=0
nombre_base10=0
#Programme de conversion base i en base 10.
for i in range (0,len(nombre)):
    n=nombre[-u]
    n=str(n)
    u=u+1
    if n.isdigit(): #Vérifie si tous les caractères sont des chiffres.
        n=int(n)
    else:
        n=ord(n)-55 #Rend le caractère à sa valeur dans la table Ascii.
    t=n*(base_i**p) 
    p=p+1
    nombre_base10=nombre_base10+t
#Sorties.
print("Le nombre",nombre,"de la base",base_i,"à la base",base_f,"est",base_final(nombre_base10,base_f))
