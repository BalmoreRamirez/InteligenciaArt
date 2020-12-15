class Perro:
    especie = 'canino'
    trucos = []

    # definimos los atributod del objeto
    def __init__(self, nombre):
        self.nombre = nombre

    # definimos la funcion
    def aprenderTrucos(self, truco):
        self.trucos.append(truco)


# creamos los dos objetos y le pasamos un nombre
perro1 = Perro('Bolt')
perro2 = Perro('Shawn')

# accedemos a su funcion y llenamos la lista
perro1.aprenderTrucos('En dos patas')
perro2.aprenderTrucos('Rodar')

print(f'Los trucos aprendidos por {perro1.nombre} son:')
print(perro1.trucos)
print(f'Los trucos aprendidos por {perro2.nombre} son: ')
print(perro2.trucos)


# segundo ejemplo

class Perro:
    especie = 'canino'
    def __init__(self, nombre):
        self.nombre = nombre
        self.trucos = []
    def aprenderTrucos(self, truco):
        self.trucos.append(truco)
perro1 = Perro('Bolt')
perro2 = Perro('Shamn')

# ensenando truco a perro 1
perro2.aprenderTrucos('En dos patas')
# ensenando trucos a perro 2
perro2.aprenderTrucos('Rueda')
# mostrar trucos aprendidos por el perro 1
print('Los trucos aprendidos por ' + perro1.nombre + 'son: ')
print(perro1.trucos)
