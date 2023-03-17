# Set sirve para definir una coleccion que no tienen indice
colors = {'Red','Green','Blue'}
print(type(colors))

print('Red' in colors)

colors.add('Purple')
print(colors)

colors.remove('Red')
print(colors)

colors.clear()
print(colors)

del colors
print(colors)