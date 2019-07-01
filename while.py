def ask(prompt):
    return int(input(prompt))

f=ask('Please give factorial which I make calculation')


def factorialR (f):
    i = 0
    f=int(f)

    while not i==(f-1):
        i=i+1
        print('to jest liczba interacji',i)
        print('to jest silnia',f)
        if f==0:
            return 1
        elif f>1:
            score=f*(f-1)
            return score
print(factorialR(f))

#------------------------------------------------------
print('------------------------------------------------')
def factorialI (f):
    silnia_tmp = 1  # zmienna pomocnicza
    if f in (0, 1):  # gdy f = 0 lub 1 zwroc 1
        return 1
    else:
        for i in range(2, f + 1):  # gdy f>1 mnoz przez kolejne liczby od 2 do f
            silnia_tmp = silnia_tmp * i
    return silnia_tmp

print(factorialI(f))


