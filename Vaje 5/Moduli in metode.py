#Napiši funkcijo najdaljsa, ki vrne najdaljšo besedo v nizu s.
"""def najdaljsa(s):
    seznam = s.split()
    return max(seznam, key=len)
print(najdaljsa('an ban pet podgan'))"""

def najdaljsa(s):
    seznam = s.split()
    najdaljsa = ""
    naj = 0
    for vsak in seznam:
        if len(vsak) > naj:
            naj = len(vsak)
            najdaljsa = vsak
    return(najdaljsa)
print(najdaljsa('an ban pet podgan'))

#Napišite funkcijo, ki izračuna podobnost med dvema nizoma.
#Podobnost definirajmo kot število mest v katerih se niza ujemata.
def podobnost(s1, s2):
    koliko = 0
    for crka in s1:
        if crka in s2:
            koliko += 1
    return koliko
print(podobnost('sobota', 'robot'))

#Napiši funkcijo, ki vrne seznam vseh sumljivih besed v danem nizu.
#Beseda je sumljiva, če vsebuje tako črko u kot črko a.
def sumljive(s):
        seznam = s.split()
        izpis = []
        for vsak in seznam:
            if "u" in vsak and "a" in vsak:
                izpis.append(vsak)
        return izpis             
print(sumljive('Muha pa je rekla: "Tale juha se je pa res prilegla, najlepša huala," in odletela.'))

#Napišite funkcijo vsi, ki sprejme seznam xs in vrne True, če so vse
#vrednosti v seznamu resnične. Elementi seznama xs so lahko poljubnega tipa, ne le bool.
def vsi(s):
    izpis = True
    for vsak in s:
        if vsak == True:
            izpis = True
        elif vsak == False:
            izpis = False
            break
    return izpis
print(vsi(['foo', 42, True]))

#Napišite funkcijo vsaj_eden, ki deluje podobno kot vsi, le da vrne True,
#če je vsaj ena vrednost v seznamu resnična.
def vsaj_eden(xs):
    izpis = False
    for vsak in xs:
        if bool(vsak) == True: #The correct way to test if something is True in a boolean context
            izpis = True
            break
    return izpis
print(vsaj_eden([2, 3, 0]))

#Vsota posameznih podseznamov.
def vsota_seznamov(s):
    seznam = []
    for vsak in s:
        vsota = 0
        for stev in vsak:
            vsota += stev
        seznam.append(vsota)
    return seznam
print(vsota_seznamov([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]))

#Napišite funkcijo, ki vrne seznam, kjer je vsako naslednje število za faktor večje od prejšnjega.
#Npr., v seznamu [1, 2, 4, 8, 16] je vsako naslednje število 2-krat večje od prejšnjega.
def mrange(start, faktor, dolzina):
    racun = start
    while dolzina > 0:
        print(racun)
        racun *= faktor
        dolzina -= 1
mrange(7, 4, 7)

