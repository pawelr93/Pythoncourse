import pickle
from os.path import exists
from pathlib import Path
def check_if_the_programme_exist():

    my_file=Path("D:\SRODOWISKO\programowanie\Python_kurs_programowanie\\baza_slangu_pickle.pckl")
    if my_file.exists():
        print('the programme exist, start working....')

    else:
        print('No exist')




def add_new_words_to_():
    """Programe which give new words into dictonary
    """

    key = input(str("Insert word to dictonary, If you want stop say \"c\" "))
    while not key == "c":
        key = input(str("Insert word to dictonary, If you want stop say \"c\" "))
        key.lower()
        # if key=="c":
        #     print("Programme finish")
        #     break
        explanation = input(str('Insert explations of this word'))
        explanation.lower()
        sciezka = "baza_slangu_pickle.pckl"
        odczytana_baza=None
        with open(sciezka, "rb") as plik:
            odczytana_baza=pickle.load(plik)
        print(odczytana_baza)
        odczytana_baza[key]=explanation
        print(odczytana_baza)
        save=odczytana_baza
        sciezka = "baza_slangu_pickle.pckl"
        with open(sciezka, "wb") as plik:
            pickle.dump(save, plik)
        sciezka = "baza_slangu_pickle.pckl"
        with open(sciezka, "rb") as plik:
            odczytana_baza2=pickle.load(plik)
        print(odczytana_baza2)
    print('exit from programme')
print(check_if_the_programme_exist())
print(add_new_words_to_())



