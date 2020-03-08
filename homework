
import random


female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
lastname = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
country = ['Poland', 'United Kingdom', 'Germany', 'France', 'Italy']


lista_slownikow = [ ]   # inicjuję pustą listę słowników


for i in range(0, 5):  # w pętli generuję wartości mające posłużyć do wypełnienia słownika, zawierającego dane kobiet


    random_firstname = random.choice(female_fnames)  # losuję imię damskie

    random_lastname = random.choice(lastname)  # losuję nazwisko

    if random_lastname == 'Kowalski':  # wylosowane dla kobiety nazwisko 'Kowalski" zmieniam na "Kowalska"
        random_lastname='Kowalska'

    random_country = random.choice(country) #  losuję kraj

    random_age = random.randint(5, 46)   #  generuję wiek

    if random_age >= 18:  # tworzę blok if-else, który na podstawie wylosowanego wieku zadecyduje, czy dana osoba jest dorosła,czy nie
        is_adult = True
    else:
        is_adult = False

    birth_year = 2019 - random_age  # na podstawie wylosowanego wieku obliczam rok urodzenia

    email = f'{random_firstname.lower()}.{random_lastname.lower()}@example.com' # z wylosowanych danych tworzę pisany małymi literami email

    slownik_K = {"firstname":random_firstname, "lastname":random_lastname, "email": email,
            "age": random_age, "country": random_country, "birth_year": birth_year, "adult": is_adult}

    # tworzę słownik zawierający dane kobiety, nazywam poszczególne klucze i przypisuję im wylosowane wartości,


    lista_slownikow.append(slownik_K)  # za każdym przejściem pętli dołączam do listy_slownikow, kolejny słownik




for i in range(0, 5):  # tworzę kolejną pętlę, w której generuję wartości potrzebne do stworzenia słownika z danymi 5 mężczyzn



    random_firstname = random.choice(male_fnames)  # losuję imię męskie

    random_lastname = random.choice(lastname)  # losuję nazwisko


    random_country = random.choice(country) #  losuję kraj

    random_age = random.randint(5, 46)   #  generuję wiek

    if random_age >= 18:  # tworzę blok if-else, który na podstawie wylosowanego wieku zadecyduje, czy dana osoba jest dorosła,czy nie
        is_adult = True
    else:
        is_adult = False

    birth_year = 2019 - random_age  # na podstawie wylosowanego wieku obliczam rok urodzenia

    email = f'{random_firstname.lower()}.{random_lastname.lower()}@example.com' # z wylosowanych danych tworzę pisany małymi literami email

    slownik_M = {"firstname":random_firstname, "lastname":random_lastname, "email": email,
            "age": random_age, "country": random_country, "birth_year": birth_year, "adult": is_adult}

    # tworzę słownik, zawierający dane mężczyzny, nazywam poszczególne klucze i przypisuję im wylosowane wartości,

    lista_slownikow.append(slownik_M)  # za każdym przejściem pętli dołączam do listy kolejny słownik


print(lista_slownikow)  # wypisuję na ekran, otrzymaną w pętli listę słowników

for n in lista_slownikow:  # dla każdego elementu listy - czyli dla każdego słownika, generuję poniższy napis


    print(f'Hi! I\'m  {n["firstname"]} {n["lastname"]}. I come from {n["country"]} and I was '
          f'born in {n["birth_year"]}. I\'m {n["age"]} years old. '
      f'My email is: {n["email"]}')
       





