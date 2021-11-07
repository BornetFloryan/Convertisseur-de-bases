def reste_divi(a,b):
    r=a%b
    return r
a=int(input("Saisir le nombre à convertir : "))
b=int(input("Saisir la base : "))
result_divi=reste_divi(a,b)
print("Le reste de la division de",a,"et",b,"est de",result_divi)


def base3_6(b):
    while base3_6(b) !=0:
        b=result_divi*b
    return b
bs3=base3_6(b)
print('En base',b,',',a,'est égale à',bs3)
