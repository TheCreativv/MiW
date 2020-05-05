# zad 8
x="Mariusz"
y='Tomek'
z='Kacper'
lista=[(x,112332),(y,113112),(z,244789)]
krotka=tuple(lista)
print(krotka)

# zad 10

num=[998777785,114114114,578968968,225225225,998777785,114114114]
lista=list(set(num))
print(lista)
            
#zad 11
listta=[]
for i in range(1,11):
    listta.append(i)
print(listta)

#zad 12
reweseList=[]
for i in range(100,19,-5):
    reweseList.append(i)
print(reweseList)

#zad 9/13
uczniowie = [
    {
        "Imię" : "Mariusz",
        'Index' : 114117,
        'Miejsce Zamieszkania' : "Olsztyn 47",
        'Telefon' : 998997996,
    },
    {
        "Imię" : "Tomek",
        'Index' : 115887,
        'Miejsce Zamieszkania' : "Iława 53",
        'Telefon' : 124785963,
    },
    {
        "Imię" : "Krzysztof",
        'Index' : 119756,
        'Miejsce Zamieszkania' : "Lubawa 17",
        'Telefon' : 147888955,
    },
    ]

for i in uczniowie:
    print("Uczeń o Imieniu {0} indexie {1} zamieszkały {2} z numerem telefonu {3}".format(
        i["Imię"],i["Index"],i['Miejsce Zamieszkania'],i['Telefon']))
