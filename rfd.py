def base_1(n,p):
    if n == 0:
        return '0'
    else:
        re = ''
        while n != 0:
            r = n % p
            if r < 10:
                result = str(r) + re
            else:
                result = chr(r + 55) + re
            n //= p
        return re
nombre = str(input("Donner nombre initiale (en base 10) : "))





for i in range (0,len(nombre)) :








# result=base_1(n,p)
# print(result)

