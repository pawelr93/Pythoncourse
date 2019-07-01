repeatHowManyTimes = int(input("Please tell me how many times to repeat..."))

for index in range(repeatHowManyTimes):
    print(index)

#Zadanie 0
print('Zadanie0')
x='Styczen\nLuty\nMarzec\nKwiecien\nMaj\nCzerwiec....'
print(x)
#zadanie 0 ver Kuba
print('zadanie 0 ver Kuba')
x=['Styczen','Luty','Marzec']
for z in x:
    print(z)
#Zadanie1
print('Zadanie1')
text = "Python is a fantastic snake"
numbercharacter=len(text)
l=range(0,numbercharacter,3)
print(l)
for idx in l:
    print(text[idx], end="")
print('#Zadanie 1.1/1.2')
#Zadanie 1.1/1.2
print('Co trzecia litera w zdaniu',text[::3])
print('#Zadanie 2')
#Zadanie 2
lista="Wypisze teraz kazda slowo osobno"
lista_slow=lista.split()
for words in lista_slow:
    print(words)
print('#Zadanie 3')
#Zadanie  3
lista=str(input('Podaj zdanie'))
lista_slow=lista.split()
for words in lista_slow:
    print(words)

for indeks, element in enumerate (lista_slow):
    print(indeks)
    print(element)