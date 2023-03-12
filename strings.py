myStr = "Hello World"

# print(dir(myStr))

# Metodos
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())

# Reemplazar 
print(myStr.replace("Hello", "bye").upper())

# Contar la cantidad de caracteres
print(myStr.count('l'))

# Saber si empieza por algun caracter
print(myStr.startswith('Hello'))

# Saber si termina por algun caracter
print(myStr.endswith('World'))

# Separar el texto ya sea por espacios o por cualquier otro caracter creando una lista
print(myStr.split("o"))

# Saber la posicion del primer valor encontrado
print(myStr.find("o"))
print(myStr.index("e"))

# Saber la longitud del string
print(len(myStr))

# Saber si el string es numerico
print(myStr.isnumeric())

# Saber si el string es alphanumerico
print(myStr.isalpha())

# Llamar el cartacter en la posicion buscada
print(myStr[4])

# Llamar el cartacter en la posicion buscada pero desde el final del string
print(myStr[-1])

# Formas de contatenar varios strings
print("Python!! " + myStr)
print(f"Python!! {myStr}")
print("Python!! {0}".format(myStr))