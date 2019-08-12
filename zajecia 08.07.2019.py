# # imie='Jola'
# # def zmien_imie():
# #     imie="Teresa"
# #     print(imie)
# # print(imie)
# # zmien_imie()
# # print(imie)
#
# def podaj_zawsze_jeden():
#     """
#     polska
#
#     :return:
#     """
#     print('jeden')
#     print('dwa')
#
#
# print(podaj_zawsze_jeden.__doc__)
# # print(podaj_zawsze_jeden())
#
#
#
#
# #zadanie 1
# def sum_of_numbers(list_of_numbers):
#     suma=0
#     for number in list_of_numbers:
#         suma=suma+number
#     return suma
#
# print(sum_of_numbers([5,9,12]))
#znajdowanie największego i najmiejszego na liscie
# def sort(numbers):
#
#     sorted_list=sorted(numbers)
#     print(sorted_list[0])
#     last=len(numbers)
#     print(numbers[last-1])
#
#
# list=[5,2,10,7]
# (sort(list))

#napisz funkcje przyjmujaca liste stringow
def return_string(stringsexample):
    newlist=[]
    lenghtofwhole=len(stringsexample)
    for i in stringsexample:
        print(len(i))
        if len(i)>2:
             newlist.append(i)
    iposition=-1
    newlist2 = []
    for i in stringsexample:

        last=len(i)

        if i[iposition+1] ==i[last-1]:
            newlist2.append(i)


    return newlist,newlist2,lenghtofwhole
print(return_string(['abc', 'xyz', 'aba', '1221']))
# #znajdujacy
# lista_a = [10,20,30,20,10,50,60,40,80,50,40]
#     if
#         count[0]
# a=set(lista_a)
# print(a)
# last=len(list_a)
#
# for i in lista_a
#     if last
simple_dict={2000:["efekt motyla","efekt motyla2"],2001:"for you baby"}
for key,value in simple_dict.items():
    print(f"podkliczem{key}jest wartośc\'{value}\'")