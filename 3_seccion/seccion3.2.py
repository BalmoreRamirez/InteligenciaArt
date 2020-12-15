# objeto clase
class DosNumeros:
    def __init__(self, num1, num2):
        self.v1 = num1
        self.v2 = num2


v = DosNumeros(2, 3)
v.v1, v.v2


# objeto instancia
class Contenedor:
    pass


x = Contenedor
x.contador = 1
while x.contador < 10:
    x.contador = x.contador + 1
    print(x.contador)
del x.contador


# objeto y metodo
class Funcion:
    def f():
        print("Hello word")


x = Funcion
conta1 = 0
while conta1 < 10:
    x.f()
    conta1 = conta1 + 1

#variables de clases e instancias
class Humano:
    especie = "Homo Sapiens"
    def __init__(self,nombre):
        self.nombre = nombre
humano1 = Humano("Jose")
humano2 = Humano('Maria')

print("Nombre: "+humano1.nombre+ "de la especie "+humano1.especie)
print("Nombre: "+humano2.nombre+ "de la especie "+humano2.especie)

#cuidado de la posicion para definir variables








