x=str(input("Give me your sentece")).lower()
print(x)
frist_letter=x[0]
last_letter=x[-1]

if frist_letter=='a':
    print('Your letter is frist letter of alphabet')
elif last_letter=='z':
    print('Your letter is last letter of alphabet')

else:
    print('Your letter is other one')
print('The founded word is school' )

term='school'

words=x.split()
print(words)
if term in words:
    print('Your word',term )

else:
    print('This senctece don t cotain this word')

lista=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(lista[1][2])