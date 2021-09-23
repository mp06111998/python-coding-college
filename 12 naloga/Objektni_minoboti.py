import unittest

class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.smer = 1
        self.ukazi = []

    #def ukazii(self):
        #return self.ukazi

    def naprej(self, d):
        if self.smer == 1: # +x
            self.x += d
            self.ukazi.append(d)
            self.ukazi.append("+x")
        elif self.smer == 2: # -y
            self.y -= d
            self.ukazi.append(d)
            self.ukazi.append("-y")
        elif self.smer == 3: # -x
            self.x -= d
            self.ukazi.append(d)
            self.ukazi.append("-x")
        elif self.smer == 4: # +y
            self.y += d
            self.ukazi.append(d)
            self.ukazi.append("+y")

    def desno(self):
        self.smer += 1
        if self.smer == 5:
            self.smer = 1
        self.ukazi.append("d")

    def levo(self):
        self.smer -= 1
        if self.smer == 0:
            self.smer = 4
        self.ukazi.append("l")
    def koordinate(self):
        return (self.x,self.y)

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if self.ukazi == []:
            True
        elif self.ukazi[-1] == "l":
            self.smer += 1
            #if self.smer == 5:
                #self.smer = 1
            self.ukazi = self.ukazi[:-1]
        elif self.ukazi[-1] == "d":
            self.smer -= 1
            #if self.smer == 0:
                #self.smer = 4
            self.ukazi = self.ukazi[:-1]
        elif self.ukazi[-1] == "+x":
            self.x -= self.ukazi[-2]
            self.ukazi = self.ukazi[:-2]
        elif self.ukazi[-1] == "-y":
            self.y += self.ukazi[-2]
            self.ukazi = self.ukazi[:-2]
        elif self.ukazi[-1] == "-x":
            self.x += self.ukazi[-2]
            self.ukazi = self.ukazi[:-2]
        elif self.ukazi[-1] == "+y":
            self.y -= self.ukazi[-2]
            self.ukazi = self.ukazi[:-2]

a = Minobot()
a.levo()
a.naprej(4)
a.desno()
a.naprej(3)
a.razveljavi()
print(a.koordinate())
#print(a.ukazii())

class TestObvezna(unittest.TestCase):
    def test_minobot(self):
        a = Minobot()
        b = Minobot()

        self.assertEqual(a.koordinate(), (0, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 0)
        self.assertEqual(b.razdalja(), 0)

        a.naprej(1)
        self.assertEqual(a.koordinate(), (1, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 1)
        self.assertEqual(b.razdalja(), 0)

        a.naprej(2)
        self.assertEqual(a.koordinate(), (3, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 3)
        self.assertEqual(b.razdalja(), 0)

        b.naprej(2)
        self.assertEqual(a.koordinate(), (3, 0))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 3)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # zdaj je obrnjen dol
        a.naprej(4)
        self.assertEqual(a.koordinate(), (3, -4))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 7)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen je levo
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -4))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 6)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen je gor
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -3))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 5)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen desno
        a.naprej(3)
        self.assertEqual(a.koordinate(), (5, -3))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 8)
        self.assertEqual(b.razdalja(), 2)

        b.levo()  # obrnjen gor
        b.naprej(3)
        self.assertEqual(b.koordinate(), (2, 3))
        self.assertEqual(b.razdalja(), 5)

        b.levo()  # obrnjen levo
        b.naprej(3)
        self.assertEqual(b.koordinate(), (-1, 3))
        self.assertEqual(b.razdalja(), 4)

        a.naprej(5)
        self.assertEqual(a.koordinate(), (10, -3))
        self.assertEqual(a.razdalja(), 13)


class TestDodatna(unittest.TestCase):
    def test_undo(self):
        a = Minobot()
        a.desno()  # gleda dol
        a.naprej(4)
        a.levo()  # gleda desno
        a.naprej(1)
        a.naprej(2)

        self.assertEqual(a.koordinate(), (3, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (1, -4))
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (1, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.naprej(1)
        self.assertEqual(a.koordinate(), (1, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.razveljavi()  # spet gleda dol
        self.assertEqual(a.koordinate(), (0, -4))
        a.naprej(2)
        self.assertEqual(a.koordinate(), (0, -6))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(3)
        self.assertEqual(a.koordinate(), (0, -3))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # spet gleda desno
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(3)
        self.assertEqual(a.koordinate(), (3, 0))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(2)
        self.assertEqual(a.koordinate(), (2, 0))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))


if __name__ == "__main__":
    unittest.main()
