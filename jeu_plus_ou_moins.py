import os
from random import randrange
a = randrange(200)
nb = int

while nb is not a:
    nb = input("choisi un nombre entre 1 et 200 : ")
    nb = int(nb)    
    if nb<a:
        print("le nombre est plus grand")
        continue
    elif nb>a:
        print("le nombre est plus petit")
        continue
    else:
        print("BRAVO")	
os.system ("pause")
