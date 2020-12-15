def salaudo():
    print('Hello word')


salaudo()


def suma(a, b):
    return a + b


resultado = suma(4, 7)
print('Resultado = ', resultado)
print(resultado, type(resultado))


def ConverertirString(numero):
    return str(numero)


def multiplicacion(num1, num2):
    res = num1 * num2
    return ConverertirString(res)


resultado = multiplicacion(2, 3)
print(resultado, type(resultado))


def principal():
    print('soy principal')
en el rodaje de una pelicula
    def secundaria():
        print('soy la segunda')

    secundaria()


principal()


def resta(num1, num2):
    return num1 - num2


resta(num2=6, num1=5)


def doble(num1, num2=2):
    return num1 * num2


doble(5)


def parametro_indeterminado(parametro1, *args):
    print(parametro1)
    for arg in args:
        print(arg)


parametro_indeterminado('hola mundo', 1, True, 0.1, 56, [0, 1, 2, 3, 4, 5])


def parametro_nombre(parametro1, *args, **kwargs):
    print(parametro1)
    for arg in args:
        print(arg)
    print(kwargs)


parametro_nombre(1, 'hola', c='parametro nombre', a=1)
