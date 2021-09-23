import random

ana_pozicija = 1
berta_pozicija = 1

vrsta = 1

while True:
    if vrsta == 1:
        met1 = random.randint(1,6)
        ana_pozicija += met1

        print("Ana vrže" ,met1, "in je na polju" ,ana_pozicija)

        if ana_pozicija >= 30:
            print("Ana je zmagala")
            break
        
        vrsta = 2
        
        if met1 == 6:
            vrsta = 1

        if ana_pozicija == berta_pozicija:
            berta_pozicija = 0
            print("Berta gre na zacetek")

    if vrsta == 2:
        met2 = random.randint(1,6)
        berta_pozicija += met2
    
        print("Berta vrže" ,met2, "in je na polju" ,berta_pozicija)

        if berta_pozicija >= 30:
            print("Berta je zmagala")
            break

        vrsta = 1

        if met2 == 6:
            vrsta = 2

        if berta_pozicija == ana_pozicija:
            ana_pozicija = 0
            print("Ana gre na zacetek")
