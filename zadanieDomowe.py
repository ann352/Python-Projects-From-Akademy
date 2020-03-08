import random


# LIST COMPREHENSION

#  - IMIONA

names = ['Ada', 'Bill', 'Yen', 'Geralt', 'Ksawery', 'Candice', 'Esmeralda']
name_lenghts = [len(name) for name in names]    # lista zawierająca dł. imion (dla każdego imienia znajdującego się w powyższej liście ,,names")
print (name_lenghts)

names_upper =[name.upper() for name in names]   # lista zawierająca imiona pisane dużymi literami
print(names_upper)


# PROMIENIE I POLA

radii = [12.1, 33, 9.3, 0.2, 190, 22.5]
pi=3.14
circle_areas = [pi * r**2 for r in radii]   # lista z polami powierzchni, wyliczonymi npdst. promieni z listy "radii"
print(circle_areas)


# ZNIŻKI

discounts = [19, 21, -5.5, 7.8, 13.1, -10.2, -21, 10.1]
another_discounts= [znizka if znizka > 0  else 0    for znizka in discounts]
print(another_discounts)


# METODY

def random_doggo():
    doggos = ['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
    dog = random.choice(doggos)
    return dog


dogX = random_doggo()
print(dogX)


# MATEMATYKA

# METODA WYLICZAJĄCA, KTÓRA Z WARTOŚCI JEST WIĘKSZA
def greater_of_pair(a,b):
    if a > b:
        return a
    else:
        return b

wynik1= greater_of_pair(3,4)
print(wynik1)



# METODA OBLICZAJĄCA ŚREDNIĄ
def average_of_3(a,b,c):
    srednia = (a+b+c) / 3
    return int(srednia)

srednia1= average_of_3(3,13,31)
print(srednia1)



#METODA ZWRACAJĄCA OKREŚLONY ELEMENT LISTY, LUB WARTOŚĆ NONE
def margins(input_list):
        if len(input_list) == 0:  # jeżeli zawartość listy jest pusta (czyli dł.listy jest równa 0)
            el_1 = None
            el_2 = None
            print("List is empty!")
            return el_1, el_2
        elif len(input_list) == 1:   # jeżeli lista ma tylko 1 element
            el_1 = input_list[0]
            el_2 = None
            return el_1,el_2
        else:                         # jeżeli lista posiada więcej niż 1 element
            el_1 = input_list[0]
            el_ostatni = input_list[-1]
            return el_1,el_ostatni



names_of_dogs=['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
print(margins(names_of_dogs))


list_with_numbers=[12.1, 33, 9.3, 0.2, 190, 22.5]
print(margins(list_with_numbers))

list_with_2elements=[3, 5]
print(margins(list_with_2elements))

lista_with_1el= ['Piłka']
print(margins(lista_with_1el))

another_list=[2]
print(margins(another_list))

empty_list=[]
print(margins(empty_list))


















