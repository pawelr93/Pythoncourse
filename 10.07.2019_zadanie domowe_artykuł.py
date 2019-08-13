from collections import defaultdict
from collections import OrderedDict
def split_words(text):
    #print(text)#tekst odczytany
    list1=text.split()
    #print(list1)#tekst podzielony
    list2=[]
    for words in list1:
        whitespace=['\'','\"','.',',','?']
        for letter in words:
            if letter in whitespace:
                words=words.replace(letter, '')
        list2.append(words)
        # print(words)
    return list2
def counting_apperance_of_words(words_by_user):

    how_many_times = 0
    for wordss in split_words(text):

        if words_by_user==wordss:
            how_many_times=how_many_times+1
        else:
            pass
    print(f'znaleziono wyraz:{words_by_user}')
    print('znaleziono go tylko:',how_many_times)

def counting_words(list2):
    dictonary_with_numbers=defaultdict(int)
    for wordss in list2:
            dictonary_with_numbers[wordss]+=1
    return dictonary_with_numbers
def TOP10_MOST_FREQUENT(dictonary_with_numbers):
    d_sorted_by_value = OrderedDict(sorted(dictonary_with_numbers.items(), key=lambda x: x[1], reverse=True))
    print('lista TOP 10 najczęściej występujących')
    i = 0
    for k, v in d_sorted_by_value.items():
        if i <10:
            print(f"pod kluczem {k} jest wartosc: {v}")
            i=i+1
def TOP10_LEAST_FREQUENT(dictonary_with_numbers):
    d_sorted_by_value1 = OrderedDict(sorted(dictonary_with_numbers.items(), key=lambda x: x[1], reverse=False))
    i = 0
    print('lista TOP 10 najmiej występujących')
    for k, v in d_sorted_by_value1.items():
        if i < 10:
            print(f"pod kluczem {k} jest wartosc: {v}")
            i = i + 1

sciezka='article1.txt'
words_by_user=(input('Wskaz slowo ktore mam ci znalesc?')).lower()
with open(sciezka,'r') as plik:
    text = plik.read().lower()
SPLIT=split_words(text)
# print(SPLIT)
COUNT=counting_words(SPLIT)
# print(COUNT)
TOP10_LEAST_FREQUENT(COUNT)
TOP10_MOST_FREQUENT(COUNT)
counting_apperance_of_words(words_by_user)

