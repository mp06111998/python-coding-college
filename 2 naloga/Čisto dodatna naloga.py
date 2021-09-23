#Ana, Berta, Cilka, Dani, Ema in Fanči
import random

zacne = random.randint(1,6)

ana = 0
berta = 0
cilka = 0
dani = 0
ema = 0
fanci = 0

while True:
    met = random.randint(1,6)

    if zacne == 1:
        if ana == 0 and met == 6:
            ana = 1
            print("Ana je vrgla 6 in je na polju 1")
        elif ana >= 1:
            ana += met
            zacne += 1

            if ana > 30:
                ana -= met
                print("Ana je vrgla preveč in je ostala na polju" ,ana)

            else:
                print("Ana vrže" ,met, "in je na polju" ,ana)
            
                if ana == berta:
                    berta = 1
                    print("Berta gre na zacetek")
                if ana == cilka:
                    cilka = 1
                    print("Cilka gre na zacetek")
                if ana == dani:
                    dani = 1
                    print("Dani gre na zacetek")
                if ana == ema:
                    ema = 1
                    print("Ema gre na zacetek")
                if ana == fanci:
                    fanci = 1
                    print("Fanci gre na zacetek")
            
                if ana == 30:
                    print("Ana je zmagala")
                    break

                if met == 6:
                    zacne = 1
        if ana == 0 and met != 6:
            zacne += 1
            print("Ana ni vrgla 6")

    elif zacne == 2:
        if berta == 0 and met == 6:
            berta = 1
            print("Berta je vrgla 6 in je na polju 1")
        elif berta >= 1:
            berta += met
            zacne += 1
            
            if berta > 30:
                berta -= met
                print("Berta je vrgla preveč in je ostala na polju" ,berta)

            else:
                print("Berta vrže" ,met, "in je na polju" ,berta)

                if berta == ana:
                    ana = 1
                    print("Ana gre na zacetek")
                if berta == cilka:
                    cilka = 1
                    print("Cilka gre na zacetek")
                if berta == dani:
                    dani = 1
                    print("Dani gre na zacetek")
                if berta == ema:
                    ema = 1
                    print("Ema gre na zacetek")
                if berta == fanci:
                    fanci = 1
                    print("Fanci gre na zacetek")

                if berta >= 30:
                    print("Berta je zmagala")
                    break

                if met == 6:
                    zacne = 2
        if berta == 0 and met != 6:
            zacne += 1
            print("Berta ni vrgla 6")

    elif zacne == 3:
        if cilka == 0 and met == 6:
            cilka = 1
            print("Cilka je vrgla 6 in je na polju 1")
        elif cilka >= 1:
            cilka += met
            zacne += 1
            
            if cilka > 30:
                cilka -= met
                print("Cilka je vrgla preveč in je ostala na polju" ,cilka)

            else:
                print("Cilka vrže" ,met, "in je na polju" ,cilka)

                if cilka == berta:
                    berta = 1
                    print("Berta gre na zacetek")
                if cilka == ana:
                    ana = 1
                    print("Ana gre na zacetek")
                if cilka == dani:
                    dani = 1
                    print("Dani gre na zacetek")
                if cilka == ema:
                    ema = 1
                    print("Ema gre na zacetek")
                if cilka == fanci:
                    fanci = 1
                    print("Fanci gre na zacetek")

                if cilka >= 30:
                    print("Cilka je zmagala")
                    break

                if met == 6:
                    zacne = 3
        if cilka == 0 and met != 6:
            zacne += 1
            print("Cilka ni vrgla 6")

    elif zacne == 4:
        if dani == 0 and met == 6:
            dani = 1
            print("Dani je vrgla 6 in je na polju 1")
        elif dani >= 1:
            dani += met
            zacne += 1

            if dani > 30:
                dani -= met
                print("Dani je vrgla preveč in je ostala na polju" ,dani)

            else:
                print("Dani vrže" ,met, "in je na polju" ,dani)

                if dani == berta:
                    berta = 1
                    print("Berta gre na zacetek")
                if dani == cilka:
                    cilka = 1
                    print("Cilka gre na zacetek")
                if dani == ana:
                    ana = 1
                    print("Ana gre na zacetek")
                if dani == ema:
                    ema = 1
                    print("Ema gre na zacetek")
                if dani == fanci:
                    fanci = 1
                    print("Fanci gre na zacetek")

                if dani >= 30:
                    print("Dani je zmagala")
                    break

                if met == 6:
                    zacne = 4
        if dani == 0 and met != 6:
            zacne += 1
            print("Dani ni vrgla 6")

    elif zacne == 5:
        if ema == 0 and met == 6:
            ema = 1
            print("Ema je vrgla 6 in je na polju 1")
        elif ema >= 1:
            ema += met
            zacne += 1

            if ema > 30:
                ema -= met
                print("Ema je vrgla preveč in je ostala na polju" ,ema)

            else:
                print("Ema vrže" ,met, "in je na polju" ,ema)

                if ema == berta:
                    berta = 1
                    print("Berta gre na zacetek")
                if ema == cilka:
                    cilka = 1
                    print("Cilka gre na zacetek")
                if ema == dani:
                    dani = 1
                    print("Dani gre na zacetek")
                if ema == ana:
                    ana = 1
                    print("Ana gre na zacetek")
                if ema == fanci:
                    fanci = 1
                    print("Fanci gre na zacetek")

                if ema >= 30:
                    print("Ema je zmagala")
                    break

                if met == 6:
                    zacne = 5
        if ema == 0 and met != 6:
            zacne += 1
            print("Ema ni vrgla 6")

    elif zacne == 6:
        if fanci == 0 and met == 6:
            fanci = 1
            print("Fanci je vrgla 6 in je na polju 1")
        elif fanci >= 1:
            fanci += met
            zacne += 1

            if fanci > 30:
                fanci -= met
                print("Fanci je vrgla preveč in je ostala na polju" ,fanci)
                zacne = 1

            else:
                print("Fanči vrže" ,met, "in je na polju" ,fanci)
                zacne = 1

                if fanci == berta:
                    berta == 1
                    print("Berta gre na zacetek")
                if fanci == cilka:
                    cilka = 1
                    print("Cilka gre na zacetek")
                if fanci == dani:
                    dani = 1
                    print("Dani gre na zacetek")
                if fanci == ema:
                    ema = 1
                    print("Ema gre na zacetek")
                if fanci == ana:
                    ana = 1
                    print("Ana gre na zacetek")

                if fanci >= 30:
                    print("Fanči je zmagala")
                    break

                if met == 6:
                    zacne = 6
        if fanci == 0 and met != 6:
            zacne += 1
            zacne = 1
            print("Fanci ni vrgla 6")
