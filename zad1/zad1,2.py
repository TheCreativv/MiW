#zadanie pierwsze
texthigh="lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
text=texthigh.lower()
lenText=len(text)
literImienia=0
literNaz=0
for litera in text:
    if litera == 'm':
        literImienia+=1
    if litera =='a':
        literImienia+=1
print(literImienia)

for litera in text:
    if litera == 'l':
        literNaz += 1
    if litera == 'i':
        literNaz += 1
    if litera == 's':
        literNaz += 1
print(literNaz)
