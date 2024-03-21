# Convertisseur de Base

Ce programme Python est un convertisseur de base qui permet de convertir un nombre d'une base initiale à une base finale. Il utilise la méthode de la division euclidienne pour effectuer la conversion.

## Démarche du Programme

Ce programme demande à l'utilisateur de fournir un nombre dans une base donnée, puis il le convertit dans la base spécifiée. Pour ce faire, le programme convertit d'abord le nombre initial en base 10 en utilisant la table ASCII pour les caractères non numériques. Ensuite, il effectue la conversion en utilisant la division euclidienne.

## Limites du Programme

Le programme respecte les contraintes définies dans le cahier des charges. Il peut convertir des nombres de la base 2 à la base 20, ne dépassant pas 20 chiffres, à l'exception des bases 2, 10 et 16. De plus, il est impossible de convertir un nombre dans sa propre base.

## Mini Manuel d'Utilisation

1. **Entrées :**
   - Fournir un nombre ne dépassant pas 20 chiffres dans la base initiale souhaitée.
   - Définir une base initiale différente de 2, 10 ou 16, comprise entre 2 et 20 inclusivement.
   - Spécifier une base finale différente de la base initiale et différente de 2, 10 ou 16, comprise entre 2 et 20 inclusivement.

2. **Exceptions :**
   - Le nombre ne doit pas dépasser 20 chiffres ni être inférieur à 1.
   - La base initiale et la base finale ne doivent pas être 2, 10 ou 16.
   - Les bases doivent être des entiers compris entre 2 et 20.
   - Les caractères ne sont pas acceptés comme entrées pour les bases.


## Auteur

Ce programme a été développé par [Floryan BORNET](https://github.com/BornetFloryan). 
