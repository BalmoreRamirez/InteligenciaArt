# clases y atributos
class Carro:
    marca = 'toyota'

miAuto = Carro
print(miAuto.marca)

# clases y sus metodos
class Auto:
    marca = 'tesla'

    def mostrarMotor():
        print('el motor del auto electrico')

miAuto2 = Auto
miAuto2.mostrarMotor()

# ambitos y espacios de nombres
def palabra():
    palabra = 'manzana'

    def localvar():
        palabra = 'uva'

    def nolocalvar():
        nonlocal palabra
        palabra = 'melon'

    def globarvar():
        global palabra
        palabra = 'sandia'

    localvar()
    print('valor de variables luego de localvar: ' + palabra)
    nolocalvar()
    print('valor de varaibles luego de nolocalvar: ' + palabra)
    globarvar()
    print('valor de variable luego de globalvar: ' + palabra)

palabra()
print('valor de varaible fuera de la clase' + palabra)
