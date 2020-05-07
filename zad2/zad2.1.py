#zad 1
listaA=[2,5,7,8,6,16,47,3]
listaB=[34,25,11,78,99,65,21,47]
listaC=[]
for numA in listaA:
    if numA%2==0:
        listaC.append(numA)
for numB in listaB:
    if numB%2!=0:
        listaC.append(numB)
print(listaC)

#zad 2
data_txt ="Lorem DoDAtkOwy tExT Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
letters=0
bigLet1=data_txt.count("D")
bigLet2=data_txt.count("O")
bigLet3=data_txt.count("G")
bigLet4=bigLet1+bigLet2+bigLet3
sLet1=data_txt.count("d")
sLet2=data_txt.count("o")
sLet3=data_txt.count("g")
sLet4=sLet1+sLet2+sLet3
for let in data_txt:
    if let == "d":
        letters+=1
    elif let == "o":
        letters+=1
    elif let == "g":
        letters+=1
    elif let == "D":
        letters+=1
    elif let == "O":
        letters+=1
    elif let == "G":
        letters+=1
text=[
    {
    "length":len(data_txt),
    "leters":letters,
    "big_letters":bigLet4,
    "small_letters":sLet4,
    },
    ]
for i in text:
    print ("długość tekstu {0}, dużych liter 'D O G' {2}, liter dużych i małych 'd o g' {1} liter małych {3}".format(i["length"],i["leters"],i["big_letters"],i["small_letters"]))
#zad 3
leter="hasło"
text="Lorem hasło Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
textL=len(text)
textR=0

for x in leter:
    for y in text:
        if x == y:
            textR+=1
result=textL-textR
for x in leter:
    for y in text:
        if x == y:
            text=text.replace(y ,"")
print("Po usunięciu powtarzających się liter zostało %d" % result)
print("Text po usunięciu \n" ,text)
    
