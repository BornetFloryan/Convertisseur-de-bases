#Projet NSI
##Convertisseur-de-bases


###•	Démarche retenue pour le programme :
Pour ce programme de convertisseur de base, j’ai choisi de demander un nombre quelconque en base choisi et de le convertir dans la base demandée. Pour cela, le programme convertit le nombre initial en base 10, en convertissant les caractères en nombres via la table Ascii, pour pouvoir le rendre en la base demandée via la division euclidienne.

###•	Les limites du programme :
Le programme suit les limites imposées par le cahier des charges. Il peut convertir tous les nombres de la base 2 à la base 20 ne dépassant pas 20 chiffres, excluant les bases 2, 10 et 16 et il est impossible de convertir la base par elle-même.

###•	Mini manuel d’utilisation :
Le programme s’utilise de façon très simple, il suffit de donner un nombre dans la base voulu et de définir la base souhaitée pour faire fonctionner la conversion. Mais cela implique quelque exception :
-	Le nombre donné ne doit pas dépasser 20 chiffres et être inférieur à 1. Il ne doit pas non plus être indéfini.
-	La base initiale doit être différente de 2, 10 ou 16. Elle ne doit pas être supérieur à 20 ou inférieur à 2. Les caractères ne sont évidemment pas acceptés.
-	La base finale doit être différente de l’initiale et de 2, 10 ou 16. Elle ne doit pas être supérieur à 20 ou inférieur à 2. Les caractères ne sont évidemment pas acceptés.
