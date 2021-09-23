from math import *

print("Potrebno je zadeti tarčo med 25 in 26 metri.")
print("============================================")
zadetek = False
while(zadetek == False):
    hitrost = int(input("Vnesi hitrost izstrelka: "))
    kot = int(input("Vnesi kot izstrelitve: "))

    rezultat = ((hitrost ** 2) * sin(2 * (kot * 3.14 / 180))) / 9.81

    tarca_min = 25
    tarca_max = 26

    if (rezultat >= tarca_min and rezultat <= tarca_max):
        print("Tarca je zadeta!")
        print("Izstrelek je pristal na razdalji" , rezultat , "metrov")
        zadetek = True
        
    else:
        print("Tarca ni zadeta, poskusi znova.")
        print("Izstrelek je pristal na razdalji" , rezultat , "metrov.")
        print("")
