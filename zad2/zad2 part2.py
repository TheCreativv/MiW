#zad 4
def Fahrenheit(celcjusz):
    far=(celcjusz*1.8)+32
    return(far)

def Rankine(celcjusz):
    ran=(celcjusz+273.15)*1.8
    return(ran)

def Kelvin(celcjusz):
    kel=celcjusz+273.15
    return(kel)
while True:
    try:
        celcjusz=int(input("Wpisz stopnie celcjusza: "))
        resultFar=Fahrenheit(celcjusz)
        resultRan=Rankine(celcjusz)
        resultKel=Kelvin(celcjusz)
        print("\n   Zamiana temperatur: \n Fahrenheit: " ,resultFar, "\n Rankine: " ,resultRan,"\n Kelvin: ",resultKel)
        print("\n")
        continue
    except:print("Podano złą wartość")
    
