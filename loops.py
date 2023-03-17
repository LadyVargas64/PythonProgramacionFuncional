foods = ['Manzana','Pera','Banano','Fresa','Arroz']

# Recorre la lista y la muestra
for food in foods:
    if food == 'Manzana':
        print('Compra 10 entonces')
    print(food)
print('-')

# Recorre la lista y la termina si encuentra un break
for food in foods:
    if food == 'Fresa':
        break
    print(food)
print('-')

# Recorre la lista y continua si en encuentra un continue pero sin mostrar el valor
for food in foods:
    if food == 'Fresa':
        continue
    print(food)

# Recorre la lista con un rango
for number in range(1, 10):
    print(number)

# Recorre la lista iterando un string
for letter in "Hello":
    print(letter)

# Recorre la lista iterando un string
count = 4
while count <= 10:
    print(count)
    count = count + 1