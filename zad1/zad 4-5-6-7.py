# zad 3
text='MetODYinzyNIeriWiEdZy'
print(dir(text))
help(text.isascii)

# zad 4

nazwa='Marisz Liszewski '
zdanie = nazwa.lower()[::-1]
 
poprzedniaLitera = ""
wynik = ""
 
for Litera in zdanie:
    if poprzedniaLitera == " ": 
        wynik += Litera.upper()
    else:
        wynik += Litera
 
    poprzedniaLitera = Litera
 
print(wynik)

#zad 5
i=0
lista=list(range(1,11))
firstList=lista[slice(5)]
print(firstList)
lastList=lista[5:10]
rewerseList=lastList[::-1]
print(rewerseList)
#zad 6
nowaLista=firstList+rewerseList
print(nowaLista)
nowaLista.insert(0,0)
print(nowaLista)
copyList = nowaLista.copy()
print(copyList)
copyList.sort(reverse = True)
print(copyList)

 


    
