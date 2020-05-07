import sys

class kalkulator():
    def __init__(self, a , b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def diff(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
class science(kalkulator):
    def exp(self):
        return self.a**self.b
while True:
    try:
        print("Aby zakończyć wciśnij dowolny klawisz oprócz cyfr. \n\n\n")
        a = int(input("Wprowadź pierwszą cyfrę: "))
        b = int(input("Wprowadź drugą cyfrę: "))
        licz=kalkulator(a,b)
        sc=science(a,b)
        zmienna=0
        while zmienna!=6:
            try:
                print("\t\t 1. Dodawanie \n \
                2. Odejmowanie \n \
                3. Mnożenie \n \
                4. Dzielenie \n \
                5. Potęgowanie \n \
                6. Wybierz inne liczby ")
                zmienna=int(input("Wprowadź cyfrę: "))

                if zmienna == 1:
                    print("Wynik dodwania: ", licz.add() )
                if zmienna == 2:
                    print("Wynik odejmowania: ", licz.diff())
                if zmienna == 3:
                    print("Wynik mnożenia: ", licz.mul())
                if zmienna == 4:
                    print("Wynik dzielenia: ", licz.div())
                if zmienna == 5:
                    print("Wynik potęgowana:  ", sc.exp())
                if zmienna == 6:
                    break
            except: print("Nie poprawny wybór!")
    except: sys.exit(0)
