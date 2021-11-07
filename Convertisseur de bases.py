#Programme division euclidienne.
def base_1(n,p):
    if n==0:
        return '0'
    else:
        re=''
        while n!=0:
            r=n%p #Calcul du reste de la division.
            if r<10:
                re=str(r)+re #Additionne le reste par le résultat.
            else:
                re=chr(r+55)+re #Convertit le nombre au caractère correspondant dans la table Ascii.
            n//=p #Division euclidienne.
        return re 
#Entrées.
nombre=str(input("Donnez nombre initiale (en base 10) ne dépassant pas 20 chiffres : ")) #Nombre à convertir en base 10 convertit en chaine.
if nombre.isdigit()== True: #Vérifie si tous les caractères sont des chiffres.
    nombre=str(nombre)
else:
    print("Entrez une valeur valide !")
    quit()
if len(nombre)>20: #Vérifie si le nombre ne dépasse pas 20 charactères.
    print("Le nombre ne doit pas dépasser 20 chiffres !")
    quit()

base_i=int(input("Donner la base initiale différente de 2, 10 ou 16 : ")) #Base initiale.
if base_i<2 or base_i>20: #Vérifie si le nombre défini n'est pas inférieur ou supérieur à 20.
    print("Veuillez saisir une base initiale qui n'est pas inférieur à 2 ou supérieur à 20 !")
    quit()
elif base_i==2 or base_i==10 or base_i==16: #Vérifie si le nombre défini ne correspond pas à 2, 10 ou 20.
    print("Les bases 2, 10 et 16 ne sont pas disponible à la conversion !")
    quit()
else:
    pass 

base_f=int(input("Donnez la base finale différente de 2, 10 ou 16 : ")) #Base finale.
if base_f<2 or base_f>20: #Vérifie si le nombre défini n'est pas inférieur ou supérieur à 20.
    print("Veuillez saisir une base finale qui n'est pas inférieur à 2 ou supérieur à 20 !")
    quit()
elif base_f==2 or base_f==10 or base_f==16: #Vérifie si le nombre défini ne correspond pas à 2, 10 ou 20.
    print("Les bases 2, 10 et 16 ne sont pas disponible à la conversion !")
    quit()
else:
    pass

u=1
e=0
nombre_1=0

for i in range (0,len(nombre)):
    n=nombre[-u]
    n=str(n)
    u=u+1
    if n.isdigit()==True: #Vérifie si tous les caractères sont des chiffres.
        n=int(n)
    else:
        n=ord(n)-55 
    t=n*(base_i**e)
    e=e+1
    nombre_1=nombre_1+t

print("Le nombre",nombre,"de la base",base_i,"à la base",base_f,"est",base_1(nombre_1,base_f))
        
    
    

