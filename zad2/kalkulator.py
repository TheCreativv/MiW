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
    
a = int(input("Wprowadź pierwszą cyfrę: "))
b = int(input("Wprowadź drugą cyfrę: "))
licz=kalkulator(a,b)
zmienna=0
while zmienna!=5:
    try:
        print("\t       1. Dodawanie \n \
              2. Odejmowanie \n \
              3. Mnożenie \n \
              4. Dzielenie \n \
              5. Zakończ ")
        zmienna=int(input("Wprowadź cyfrę: "))

        if zmienna == 1:
            print("Wynik dodwania: ", licz.add())
        if zmienna == 2:
            print("Wynik odejmowania: ", licz.diff())
        if zmienna == 3:
            print("Wynik mnożenia: ", licz.mul())
        if zmienna == 4:
            print("Wynik dzielenia: ", licz.div())
        if zmienna == 5:
            break
    except: print("Nie poprawny wybór!")
