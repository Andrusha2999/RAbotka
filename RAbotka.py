from module1 import *
while True:
    print("Funktsioonid".center(50,"+"))
    v=input("arithmetic- A, \nis_year_leap- B, \nsquare- C, \nseason- D, \nbank- E, \nkodeeriumine- x")
    if v.upper()=="A":
        a=float(input("Arv 1: "))
        b=float(input("Arv 2: "))
        c=input("Tehe: ")
        result=arithmetic(a,b,c)
        print(result)
    elif v.upper()=="B":
        year=int(input("Sisesta aasta: "))
        result=is_year_leap(year)
        print(result)
    elif v.upper()=="C":
        kv=int(input("Sisestage ruudu külg: "))
        result=square(kv)
        print(result)
    elif v.upper()=="D":
        kuu=int(input("Sisestage kuu number: "))
        result=season(kuu)
        print(result)
    elif v.upper()=="E":
        a=float(input("Sisestage sissemakse summa: "))
        years=int(input("Mitu aastat on möödunud?"))
        result=bank(a,years)
        print(result)
    elif v.upper()=="F":
        a=int(input("Sisestage number: "))
        result=is_prime(a)
        print(result)
    elif v.upper()=="x":
        print("Kodeeremine".center(60,"*"))
        rezult=xor_cipher(input("sisesta text"),input("sisesta võti:"))
        print(rezult)
        print("dekoderiumine".center(60,"*"))
        de_rezult=xor_ciper(input("sisesta võti")
        print(de_rezult)
