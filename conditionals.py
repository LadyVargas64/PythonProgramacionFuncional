x = 20

if x > 30:
    print("x es mayor que 30")
else:
    print("x es menor que 30") 

color = 'aqua'

if color == "blue":
    print('El color es azul')
elif color == "red":
    print('El color es rojo')
else:
    print('Es otro color')

name = "Jhon"
lastName = "Carter"

if name == "Jhon":
    if lastName == "Carter":
        print("Tu eres Jhon Carter")
    else:
        print("Tu no eres Jhon Carter") 
else:
    print('Tu eres Jhon')

x = 5
y = 10

if(x > 2 and x <= 10):
    print("x es mayor que 2 y menor o igual a 10")
if(x > 2 or x <= 20):
    print("x es mayor que 2 o menor o igual a 20")
if(not(x == y)):
    print("x no es igual a y")