# estrucutura de control
# IF
numero = 1
if numero == 1:
    print('El numero es un uno')

# if else
numero = 2
if numero == 1:
    print('el  numero es 1')
elif numero == 2:
    print('el numero es 2')
elif numero == 3:
    print('el numero es 3')

# while = mientras
var1 = 10
while var1 > 2:
    print('El valor de la variable es: ' + str(var1))
    var1 -= 1

# break
var2 = 10
while var2 > 0:
    print('El valor de la variable es: ' + str(var2))
    if var2 == 4:
        print('se encontro un 4, saliendo del bucle')
        break
    var2 -= 1
# continue
var3 = 10
while var3 > 0:
    var3 -= 1
    if var3 == 4:
        print(' se encontro un 4, salta al siguiente ciclo...')
        continue
    print('el valor de la variable es: ' + str(var3))
# else
var4 = 10
while var4 > 0:
    var4 -= 1
    print('el valor de la variable es: ' + str(var4))
else:
    print('el ciclo ha terminado')

# for
name = 'Programador'
counter = 0
for x in name:
    counter += 1
    print('La letra #' + str(counter) + 'es ' + x)

# agregamos un else
name1 = 'Alejandro'
counter1 = 0
for x in name1:
    counter1 += 1
    print('La letra # ' + str(counter1) + ' es ' + x)
else:
    print('Nombre recorrido por completo')

# rrecoriendo una lista con el for
names = ['jose', 'fatima', 'jasmin']
counter4 = 0
for x in names:
    counter4 += 1
    counter5 = 0
    print('El nombre #' + str(counter4) + ' es ' + x)
    print('sus letras son: ')
    for y in x:
        counter5 += 1
        print('Letra #' + str(counter4) + ': ' + y)
else:
    print('finalizo')

# utilizando la funcion break
names = ['julio', 'fatima', 'jasmin']
counter4 = 0
for x in names:
    counter4 += 1
    counter5 = 0
    print('El nombre #' + str(counter4) + 'es ' + x)
    print('sus letras son: ')
    for y in x:
        counter5 += 1
        if y == 'a':
            print('se encontro la letra a, deteniedo el bucle....')
            break
        print('letra #' + str(counter5) + ': ' + y)
    else:
        print('bucle fianlizado')
# utilizando la funcion continue
for x in names:
    counter4 += 1
    counter5 = 0
    print('El nombre #' + str(counter4) + 'es ' + x)
    print('sus letras son: ')
    for y in x:
        counter5 += 1
        if y == 'a':
            print('omitiendo impresion de letra a')
            continue
        print('Letra #' + str(counter5) + ': ' + y)
    else:
        print('bucle finalizado')
# utilizando la funcion rango
for x in range(5):
    print('Repeticion #' + str(x))

# utilizando valores en rango
for x in range(1, 6):
    print('Repeticion #' + str(x))

# valor del incremento
for x in range(1, 8, 2):
    print('repericion #' + str(x))
