# definir una funcion 
def hello():
    print('Hello')

hello()

# definir una funcion con parametros
def hello2(name):
    print('Hello '+name)

hello2("Ryan")
hello2("Lady")

# definir una funcion con parametros y estos con un valor definido
def hello3(name = "Person"):
    print('Hello '+name)

hello3("Yohana")
hello3()


# definir una funcion haciendo una suma de 2 valores 
def add(num1, num2):
    return num1 + num2

print(add(10,6))

# Funcion Lambda: funcion anonima que toma un numero de 
# argumentos pero son escritos utilizando una expresion
suma = lambda num1, num2: num1 + num2
print(suma(1,5))