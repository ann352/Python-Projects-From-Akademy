animals = ['dog', 'cat', 'fish', 'monkey', 'elephant']

for animal in animals:
    print(animal.capitalize())

animals.append('horse')
print(animals)

for animal in animals: #przejscie po wszystkich elementach
    print(animal.capitalize())
  # na stringach w pętli można wykonywać funkcje

for n in range (1,11):  #pętla przejdzie od 1 do 10 włącznie
    print(n*2)  # wydrukuje każdy element * 2

for n in range(10, 31):  # pętla przejdzie od 10 do 30 włącznie
    print(n * 4)  # wydrukuje każdy element * 4

#1.pusta lista numbers
#petla 20 do 30
#w kazdej iteracji dołączam 3
#print numbers

numbers= [0]
for number in range (20,31):
    numbers.append(number)

print(numbers)


