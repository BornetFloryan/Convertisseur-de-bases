def conv_dix(n,p):
    dix = ""
    while (n !=0):
        dix+=str(n%p)
        n=n//p
    return dix [::-1]


n=int(input("Donner un nombre en base 10 : "))
p=int(input("Donner la base: "))
result=conv_dix(n,p)
print(result)




    