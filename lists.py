demoLlist = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red','blue','yellow']

numberList = list((1, 2, 3, 4))
print(numberList)
print(type(numberList))

# Obtener el rabgo de 1 a 9
r = list(range(1, 10))
print(r)

# Saber los metodos que pueden hacerle con un list
print(dir(colors))

# Saber la longitud de list
print(len(colors))

# Saber el valor de una posicion de un list
print(colors[1])

# Saber el valor esta en  un list devolviendo un booleano
print('green' in colors)

# Cambiar un valor del list
colors[1] = 'violet'
print(colors)

# Agregar un nuevo valor a la lista
colors.append('aqua')
print(colors)

# Agregar varios valores a la lista
colors.extend(['blue','orange'])
print(colors)

# Agregar un valor en una posicion dada
colors.insert(1, 'black')
print(colors)

# Quitar el ultimo valor de una list o por la posicion
colors.pop()
colors.pop(1)
print(colors)

# Quitar un elemento de una lista dependiendo de su valor
colors.remove('red')
print(colors)

# Limpiar la lista
# colors.clear()
# print(colors)

# Ordenar la lista a - z
colors.sort()
print(colors)

# Ordenar la lista z - a
colors.sort(reverse=True)
print(colors)

# Saber el index con respecto al valor
print(colors.index('aqua'))

# Saber la cantidad de elementos con respecto al valor
print(colors.count('aqua'))