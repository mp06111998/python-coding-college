#Napišite funkcijo naj(xs), ki vrne največje število v seznamu xs.
def naj(xs):
    najvecja = xs[0]
    for i in xs:
        if i >= najvecja:
            najvecja = i
    return najvecja
print(naj([5, 1, -6, -7, 2]))

#Napišite funkcijo naj_abs(xs), ki vrne največje število po absolutni vrednost v seznamu xs.
def naj_abs(xs):
    najvecja = xs[0]
    for i in xs:
        if abs(i) >= abs(najvecja):
            najvecja = i
    return najvecja
print(naj_abs([5, 1, -6, -7, 2]))

#Napišite funkcijo ostevilci(xs), ki vrne seznam oblike [(0, xs[0]), (1, xs[1]),
#..., (n, xs[n])]. n je enak dolžini seznama xs minus ena.
def ostevilci(xs):
    seznam = []
    for i in range (len(xs)):
        seznam.append((i, xs[i]))
    return seznam
print(ostevilci([5, 1, 4, 2, 3]))

#Napišite funkcijo prastevila(n), ki ugotovi, koliko praštevil je manjših od števila n.
#Praštevila manjša od 10 so 2, 3, 5 in 7.
def prastevila(n):
    koliko = 0
    for i in range (n):
        i += 1
        deliteljev = 0
        for j in range (i):
            j += 1
            if i % j == 0:
                deliteljev += 1
        if deliteljev == 2:
            koliko += 1
    return koliko
print(prastevila(10))
#Rešitev na učilnici.
"""import math
def prastevila(n):
    cnt = 0
    for j in range(2, n):
        for i in range(2, int(math.sqrt(j)) + 1):
            if j % i == 0:
                break
        else:
            cnt += 1
    return cnt"""

#Napišite funkcijo palindrom(s), ki preveri, ali je niz s palindrom.
def palindrom(s):
    return s == s[::-1]
print(palindrom("pericarežeracirep"))
print(palindrom("kolo"))

#Napišite funkcijo an_ban_pet_podgan(xs), ki za seznam xs poišče zmagovalca v izštevanki
#"An ban pet podgan". Zmagovalec igre je tisti, ki na koncu edini ostane neizločen.
def an_ban_pet_podgan(xs):
    i = 0
    for j in range(len(xs) - 1):
        i = (i + 10) % len(xs)
        xs.pop(i)
    return xs[0]
print(an_ban_pet_podgan(["Maja", "Janja", "Sabina", "Ina", "Jasna"]))
print(an_ban_pet_podgan(["Maja", "Janja", "Sabina"]))
